### Summary

This is a follow up of the now closed DR 423 which resulted in the clarification
of the status of qualifications of rvalues.

This defect report aims to clarify the status of the controlling expression of
`_Generic` primary expression:

***Does the controlling expression of a `_Generic` primary expression undergo
any type of conversion to calculate the type that is used to do the
selection?***

Implementers have given different answers to this question; gcc (*choice 1* in
the following) on one side and clang and IBM (*choice 2*) on the other side went
quite opposite ways, resulting in severe incompatibility for `_Generic`
expression that use qualifiers or arrays.

```c
char const* a = _Generic("bla", char*: "blu");                 // clang error
char const* b = _Generic("bla", char[4]: "blu");               // gcc error
char const* c = _Generic((int const){ 0 }, int: "blu");        // clang error
char const* d = _Generic((int const){ 0 }, int const: "blu");  // gcc error
char const* e = _Generic(+(int const){ 0 }, int: "blu");       // both ok
char const* f = _Generic(+(int const){ 0 }, int const: "blu"); // both error
```

The last two lines, where gcc and clang agree, points to the nature of the
problem: gcc treats all such expressions as rvalues and does all applicable
conversions of 6.3.2.1, that is lvalue to rvalue and array to pointer
conversions. clang treats them as lvalues.

### Problem discussion

The problem arises to know whether or not the conversions of 6.3 apply to the
controlling expression.

* **promotions:** There is no general rule to which expressions these apply, but their application is hard coded for the individual operators, where it makes reference to "its (promoted) operand".
* **lvalue conversion:** I didn't find any text that would impose lvalue conversion performed to the controlling expression. All wording in 6.3 is "some" and "may". Also it talks of "operators" and "operations", but `_Generic` is not an operator, but a primary expression. The wording in 6.5.1.1 is *has a type* and doesn't make any reference to type conversion.
* **array conversion:** The support for array conversion is stronger. Array conversion has an explicit list of cases (*6.3.2.1 p3*) were an array is an *operand* where it doesn't apply. But
  + The case of arrays as an exception in *6.3.2.1 p3* doesn't list the *associations* of `_Generic` either, which are listed in *6.5.1.1*.
  + There is another precedent, namely *parenthesized expressions*, which are also not listed in *6.3.2.1 p3* and where nobody expects an array conversion, either.

#### Integer promotions

Applying promotions would have as an effect that we wouldn't be able to
distinguish narrow integer types from `int`. There is no indication that the
text implies that form or conversion, nor that anybody has proposed to use
`_Generic` like this.

#### Choice 1: Consequences of lvalue conversion

All conversion in *6.3.2.1 p2* describe what would in normal CS language be
named the evaluation of an object. It has no provision to apply it to types
alone. In particular it includes the special clause that uninitialized
`register` variables lead to undefined behavior when undergoing lvalue
conversion. As a consequence:

*Any lvalue conversion of an uninitialized `register` variable leads to
undefined behavior.*

And thus

***Under the hypothesis that the controlling expression undergoes lvalue
conversion, any `_Generic` primary expression that uses an uninitialized
`register` variable as controlling expression leads to undefined behavior.***

#### Choice 2: Consequences not doing conversions

In view of the resolution of DR 423 (rvalues drop qualifiers) using `_Generic`
primary expressions with objects in controlling expression may have results that
appear surprising.

```c
#define F(X) _Generic((X), char const: 0, char: 1, int: 2)
char const strc[] = "";
F(strc[0])   // -> 0
F(""[0])     // -> 1
F(+strc[0])  // -> 2
```

So the problem is here, that there is no type agnostic operator that results in
a simple lvalue conversion for `char const` objects to `char`; all such
operators also promote `char` to `int`.

***Under the hypothesis that the controlling expression doesn't undergo
conversion, any `_Generic` primary expression that uses a qualified lvalue of
narrow type `T` can't directly trigger the association for `T` itself.***

#### non-equivalence of the two approaches

For many areas the two approaches are feature equivalent, that is both allow to
implement the same semantic concepts, but with different syntax. Rewriting code
that was written with one of choices in mind to the other choice is in general
not straight forward and probably can't be automated.

* Code that was written with *choice 1* in mind (enforced lvalue and array conversion) when translated to *choice 2* has to enforce such conversions. E.g as long as we know that the type of `X` is only a wide integer type or an array or pointer type, a macro such as

  ```c
          #define bla(X) _Generic((X), ... something ... )
  ```

  would have to become

  ```c
          #define bla(X) _Generic((X)+0, ... something ... )
  ```

  Writing code that takes care of narrow integer types is a bit more difficult, but can be done with 48 extra case selections, taking care of all narrow types (6) and all their possible qualifications (8, `restrict` is not possible, here). Code that uses `struct` or `union` types must use bizarre things like `1 ? (X) : (X)` to enforce lvalue conversion.

  ```c
          #define blaOther((X),                                  \
            char: blub, char const: blub, ...,                   \
            short: ...,                                          \
            default: _Generic(1 ? (X) : (X), struct toto: ... )

          #define bla(X) _Generic((X)+0, ... something ... ,     \
            default: blaOther(X))
  ```
* Code that was written with *choice 2* in mind (no lvalue or array conversion) when translated to *choice 1* has to pass to a setting where qualifiers and arrays are preserved in the type. The only such setting is the address-of operator `&`.

  ```c
          #define blu(X) _Generic((X), \
             char const: blub,         \
             char[4]: blob,            \
             ...)
  ```

  has to be changed to something like

  ```c
          #define blu(X) _Generic(&(X),\
            char const*: blub,         \
            char(*)[4]: blob,          \
            ...)
  ```

  That is each individual type selection has to be transformed, and the syntactical change that is to be apply is no simple textual replacement.

### Application work around

Since today C implementations have already taken different paths for this
feature, applications should be careful when using `_Generic` to remain in the
intersection of these two interpretations. A certain number of design questions
should be answered when implementing a type generic macro:

* Do I want to differentiate the outcome according to the qualification of the argument?
* Do I want to distinguish arrays from pointer arguments?
* Do I want to distinguish narrow types?
* Do I want to apply it to composite types, namely `struct` types?

The following lists different strategies for common scenarios, that can be used
to code type generic macros that will work with both of the choices 1 or 2\.

#### Wide integers and floating point types

This is e.g the case of the C library interfaces in `<tgmath.h>`. If we know
that the possible type of the argument is restricted in such a way, the easiest
is to apply the unary plus operator `+`, as in

```c
  #define F(X) _Generic(+(X),             \
    default: doubleFunc,                  \
    int: intFunc,                         \
    ...                                   \
    _Complex long double: cldoubleFunc)(X)

  #define fabs(X) _Generic(+(X),          \
    default: fabs,                        \
    float: fabsf,                         \
    long double: fabsl)(X)
```

This `+` sign ensures an lvalue to rvalue conversion, and, that it will error
out at compilation time for pointer types or arrays. It also forcibly promotes
narrow integer types, usually to `int`. For the later case of `fabs` all integer
types will map to the `double` version of the function, and the argument will
eventually be converted to `double` before the call is made.

#### Adding pointer types and converting arrays

If we also want to capture pointer types *and* convert arrays to pointers, we
should use `+0`.

```c
  #define F(X) _Generic((X)+0),           \
    default: doubleFunc,                  \
    char*: stringFunc,                    \
    char const*: stringFunc,              \
    int: intFunc,                         \
    ...                                   \
    _Complex long double: cldoubleFunc)(X)
```

This binary `+` ensures that any array is first converted to a pointer; the
properties of `0` ensure that this constant works well with all the types that
are to be captured, here. It also forcibly promotes narrow integer types,
usually to `int`.

#### Converting arrays, only

If we k now that a macro will only be used for array and pointer types, we can
use the `[]` operator:

```c
  #define F(X) _Generic(&((X)[0]),        \
    char*: stringFunc,                    \
    char const*: stringFunc,              \
    wchar_t*: wcsFunc,                    \
    ...                                   \
    )(X)
```

This operator only applies to array or to pointer types and would error if
present with any integer type.

#### Using qualifiers of types or arrays

If we want a macro that selects differently according to type qualification or
according to different array size, we can use the `&` operator:

```c
  #define F(X) _Generic(&(X),        \
    char**: stringFunc,              \
    char(*)[4]: string4Func,         \
    char const**: stringFunc,        \
    char const(*)[4]: string4Func,   \
    wchar_t**: wcsFunc,              \
    ...                              \
    )(X)
```

### Possible solutions

The above discussion describes what can be read from the text of C11, alone, and
not the intent of the committee. I think if the committee would have wanted a
*choice 2*, the standard text would not have looked much different than what we
have, now. Since also the intent of the committee to go for *choice 1* seems not
to be very clear from any additional text (minutes of the meetings, e.g) I think
the reading of *choice 2* should be the preferred one.

### Suggested Technical Corrigendum (any choice)

Amend the list in footnote 121 for objects with `register` storage class. Change

> Thus, the only operators that can be applied to an array declared with
> storage-class specifier `register` are `sizeof` and `_Alignof`.

<ins>Thus, an identifier with array type and declared with storage-class
specifier `register` may only appear in primary expressions and as operand to
`sizeof` and `_Alignof`.</ins>

### Suggested Technical Corrigendum (Choice 2\)

Change 6.5.1.1 p3, first sentence

> The controlling expression of a generic selection is not evaluated <ins>and the
> type of that expression is used without applying any conversions described in
> Section 6.3</ins>.

Add `_Generic` to the exception list in *6.3.2.1 p3* to make it clear that array
to pointer conversion applies to none of the controlling or association
expression if they are lvalues of array type.

> Except when it is <ins>the controlling expression or an association expression
> of a `_Generic` primary expression, or is</ins> the operand of the `sizeof`
> operator, the `_Alignof` operator, or the unary `&` operator, or is a string
> literal used to initialize an array, an expression that has type “array of type”
> is converted to an expression with type “pointer to type” that points to the
> initial element of the array object and is not an lvalue. If the array object
> has register storage class, the behavior is undefined.

Also add a forward reference to `_Generic` in 6.3.2.

### Suggested Technical Corrigendum (Choice 1\)

If the intent of the committee had been *choice 1* or similar, bigger changes of
the standard would be indicated. I only list some of the areas that would need
changes:

* Move `_Generic` from primary expressions to a proper subsection, and rename the feature to `_Generic` operator.
* Clarify which *as-if* conversions must be applied to determine the type.
* Reformulate those conversions as conversions of types instead of values.

Also, add `_Generic` to the exception list in *6.3.2.1 p3* to make it clear that
array to pointer conversion applies to none of the association expression if
they are lvalues of array type.

> Except when it is <ins>an association expression of a `_Generic` expression, or
> is</ins> the operand of the `sizeof` operator, the `_Alignof` operator, or the
> unary `&` operator, or is a string literal used to initialize an array, an
> expression that has type “array of type” is converted to an expression with type
> “pointer to type” that points to the initial element of the array object and is
> not an lvalue. If the array object has register storage class, the behavior is
> undefined.

### Suggested Technical Corrigendum (Status quo)

A third possibility would be to leave this leeway to implementations. I strongly
object to that, but if so, I would suggest to add a phrase to 6.5.1.1 p3 like:

> ... in the default generic association. <ins>Whether or not the type of the
> controlling expression is determined as if any of conversions described in
> Section 6.3 are applied is implementation defined.</ins> None of the expressions
> ...
