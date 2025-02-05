### Summary

The dealing of rvalues with qualified types is largely underspecified in all
versions of the C standard. This didn't surface as a problem until C11, since
until then the type of an expression was not observable but only its value.

With C11 now a problem arises for type generic primary expressions; with
`_Generic` type qualifications of values have become observable.

The standard in any of its versions has not much to say when it comes to
qualified types for rvalues. They definitively do exist, since the cast operator
(6.5.4p2) explicitly specifies that the type could be qualified. That section on
casts also has the only indication that relates to rvalues. There is a footnote
(thus not normative) that says

> 89\) A cast does not yield an lvalue. Thus, a cast to a qualified type has the
> same effect as a cast to the unqualified version of the type.

That could mean two things:

1. the effective type of the resulting rvalue is unqualified
2. all operators that will accept the rvalue as an operand will act all the same whether the type is qualified or not

doing some tests I have found that clang and gcc disagree on this point. (gcc
doesn't have `_Generic`, yet, but other builtins to observe types)

clang seems to implement 1., gcc 2\. They agree for lvalues like this

```c
_Generic((double const){ 0 },
         default: 0,
         double const: 1)
```

both evaluate it to `1`.

They disagree on the outcome for rvalues

```c
_Generic((double const)0,
         default: 0,
         double const: 1)
```

clang gives `0`, gcc gives `1`.

(for gcc all with caution that it doesn't have `_Generic` yet, but that this was
obtained using an emulation of it by means of other gcc builtins)

So that situation can easily lead to simple programs that have a behavior that
depends on an undocumented choice and thus observe *unspecified behavior*.

### Discussion

#### Importance of observability of qualifiers

This is not a defect of the `_Generic` construct itself. The intention is
clearly to distinguish all types (with the exception of VM types) that are not
compatible, thus to allow to distinguish all 8 different forms of qualifications
of a type (resp. 16 for pointer types) that can be obtained from the qualifiers
`_Atomic`, `const`, `volatile` (and `restrict`).

For type generic expressions that are intended to operate on lvalues, such
distinction can be crucial for any of the four qualifiers:

* For `const` or `volatile` qualified lvalues there might be situations where application code might want to use an unqualified compound literal in place of the controlling expression.
* For `_Atomic` qualified lvalues there might be situations where application code might want to select a different function than for expressions with same base type but without such a qualifier.
* `restrict` (or not) qualified pointers may enable an application to select different algorithms or functions (e.g `memcopy` versus `memmove`).

#### Lvalue conversion of the controlling expression of the generic selection is not a solution

Up to now, the conversions of 6.3.2.1 do not apply to primary expressions but
only to operators. E.g in the following

```c
double A[5];
double (*B)[5] = &A;
double (*C)[5] = &(A);
```

`B` and `C` should be initialized to the same value, the address of `A`. If in
`(A)` the primary expression `()` would enforce a decay of the array to a
pointer (and thus to an rvalue) the initialization expression for `C` would be a
constraint violation.

So it seems obvious that the conversions in 6.3.2 ("Other Operands") are not
intended to be applied to primary expressions.

Also the conversions in 6.3.2 are not consistent with respect to qualifiers. The
only conversion that explicitly drops qualifiers is lvalue conversion
(6.3.2.1p2). Array to pointer conversion (6.3.2.1p3) doesn't change qualifiers
on the base type. Pointer conversion then, in 6.3.2.3, may add qualifiers to the
base type when converting.

#### Origin

Two different constructs can be at the origin of a qualification of an rvalue:

* casts, but only for scalar types
* function evaluation, resulting in any type but an array or function type.

Both constructs explicitly allow for qualifiers to be applied to the type. In
particular 6.7.6.3p15 emphasizes (and constrains) the return type of function
specifications to have compatible types, thus indicating that the qualification
of the return type bares a semantic meaning.

#### Operations

If we suppose that any rvalue expression carries its qualification further,
other operations (e.g unary or binary `+`) could or could not result in
qualified rvalues. The conversion rules in 6.3 and in particular the usual
arithmetic conversions in 6.3.1.8 that allow to determine a common real type
don't specify rules to deal with qualifiers.

It seems that a lot of compilers already warn on such "superfluous"
qualifications, but in view of type generic primary expression it is not clear
that such warnings are still adequate.

#### Comparison to C\+\+

C\+\+ had to resolve this problem since its beginnings, because the feature of
function overloading together with references of rvalues had made rvalue types
and their qualifications observable.

Interestingly, to solve the problem the C\+\+ refers to the C standard, claiming
that C would drop all qualifiers for rvalue expressions that have scalar base
type. It does this without refering to a particular text in the C standard, and
in fact it can't since there doesn't seem to be such text.

The actual solution in C\+\+ is thus that all rvalue expressions of non-scalar
types are `const`-qualified and that those of scalar types are unqualified. In
view that scalar types are exactly those types that are allowed to have cast
operators that qualify the type, all of this looks like a useless additional
complication of the issue.

### Suggested Technical Corrigendum

There doesn't seem to be an easy solution to this defect, and the proposed
solutions (as below or even differently) probably will need some discussion and
investigations about their implications on existing code before a consensus
could be reached.

#### Proposal 1: Require the implementation to specify its choice

This is (to my opinion) the worst solution, because the potential different code
paths that an application code could take are numerous. There are 4 different
qualifiers to handle and code that would have to rely on enumerating all
combinations of different generic choices can quickly become a maintenance
nightmare.

Also, implementations that chose to keep qualifiers on rvalues would have to
decide (and document) by their own what the rules would be when operators are
applied to such qualified rvalues.

#### Proposal 2: Keep all qualifiers on types of rvalue expressions

For this solution in should be then elaborated how operators handle qualifiers.
A natural way would be to accumulate qualifiers from operands with different
qualifiers.

An important issue with this approach is the rapidly increasing number of cases,
in particular 16 for pointer types. To keep the number of cases low when
programming with type generic expressions we would need a *generic* tool for the
following:

How to drop qualifiers for type generic expressions? Or alternatively add all
qualifiers?

For arithmetic types with base type other than `_Bool`, `char`, or `short`
something like the following would be useful:

```c
+(X)                                 // if unary plus drops all qualifiers
(X) + (int const volatile _Atomic)0  // if qualifiers accumulate
```

This strategy wouldn't work for the narrow types, because the are promoted to
`signed` or `unsigned`.

#### Proposal 3: Require the implementation to provide a feature test macro

This solution would already be a bit better than the previous one, since
applications that compose type generic macros could select between two (or
several) implementations. But the main problems (complexity and
underspecification of operations) would remain.

#### Proposal 4: Drop all qualifiers from the controlling expression of the generic selection

This is not an ideal solution, since it would remove a lot of expressiveness
from the generic selection construct. Lvalues could no be distinguished for
their qualifiers:

```c
void f(double*);
#define F(X) _Generic((X), double: f)(&(X))

double const A = 42;
F(A);
```

Here dropping the qualifiers of `A` would result in a choice of `f` and in the
evaluation of `f(&A)`. In case that `f` modifies its argument object (which we
can't know) this would lead to undefined behavior.

Not dropping the qualifiers would lead to a compile time constraint violation,
because none of the types in the type generic expression matches. So here an
implementation would be forced to issue a diagnostic, whereas if qualifiers are
dropped the diagnostic is not mandatory.

#### Proposal 5: Drop all qualifiers of rvalues

This solution seems the one that is chosen by clang. It is probably the easiest
to specify. As mentioned above it has the disadvantage that the two very similar
expressions `(int const){0}` and `(int const)0` have different types.

Some clarification should be added to the standard, though.

<ins>6.5.1.1, modify as follows:  
EXAMPLE The `cbrt` type-generic macro could be implemented as follows. Here the
prefix operator `+` in the selection expression ensures that lvalue conversion
on arithmetic types is performed such that e.g lvalues of type `float const`
select `cbrtf` and not the default `cbrt`.</ins>

```c
#define cbrt(X) _Generic(+(X), \
long double: cbrtl,            \
default: cbrt,                 \
float: cbrtf                   \
)(X)
```

<ins>6.5.2.2, add after p1: The type of a function call is the return type of
the function without any qualifiers.</ins>

<ins>6.5.4, add after p2: The type of a cast expression of a qualified scalar
type is the scalar type without any qualifiers.</ins>

<ins>6.7.63, change p15, first sentence: For two function types to be
compatible, the unqualified versions of both return types shall be
compatible.</ins>

**C11:** When introduced like this, this will invalidate some valid C11
programs, since some type generic expression might behave differently. The
faster such corrigendum is adopted the less likely it is that such programs
exist.

#### Proposal 6: Add a `const` qualifier to all types for rvalues

Analogous as in the case above it has the disadvantage that the two very similar
expressions `(int){0}` and `(int)0` have different types.

This is my favorite solution, since it also "repairs" another issue that I am
unconfortable with: the problem of array decay in objects with temporary
lifetime:

```c
  struct T { double a[4]; } A;
  struct T f(void) { return (struct T){ 0 }; }
  double g0(double* x) { return *x; }
  ...
  g0(f().a);
```

Here `f()` is an rvalue that results in an object of temporary lifetime `struct
T` and then `f().a` decays to a `double*`. Semantically a better solution would
be that it decays to a `double const*` since a modification of the value is not
allowed (undefined behavior). Already with C99 it would be clearer to declare
`g1` as:

```c
  double g1(double const* x) { return *x; }
```

If `f()` would be of type `struct T const`, `f().a` would decay to a `double
const*`. Then a call of `g0` would be a constraint violation and `g1` would have
to be used.

The necessary changes to the standard would be something like:

<ins>6.5.1.1, modify as follows:  
EXAMPLE The `cbrt` type-generic macro could be implemented as follows. Here the
prefix operator `+` in the selection expression ensures that lvalue conversion
on arithmetic types is performed such that e.g lvalues of type `float` select
`cbrtf` and not the default `cbrt`.</ins>

```c
#define cbrt(X) _Generic(+(X), \
long double const: cbrtl,      \
default: cbrt,                 \
float const: cbrtf             \
)(X)
```

<ins>6.5.2.2, add after p1: The type of a function call is the `const`-qualified
return type of the function without any other qualifiers.</ins>

<ins>6.5.4, add after p2: The type of a cast expression of a qualified scalar
type is the `const`-qualified scalar type without any other qualifiers.</ins>

The third addedum would be the same as in the previous case:

<ins>6.7.63, change p15, first sentence: For two function types to be
compatible, the unqualified versions of both return types shall be
compatible.</ins>

**C11:** When introduced like this, this will invalidate some valid C11
programs, since some type generic expression might behave differently. The
faster such corrigendum is adopted the less likely it is that such programs
exist.

**C99:** When introduced like this, this will invalidate some valid C99 programs
that pass rvalue pointers as presented above to function parameters that are not
`const`-qualified but where the called function then never modifies the object
of temporary lifetime behind the pointer. Unless for very old legacy functions
(from before the introduction of `const` to the language) such interfaces should
be able to use the "correct" `const`-qualification, or they could be overloaded
with a type generic interface that takes care of that issue.
