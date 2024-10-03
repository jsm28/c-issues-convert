### Summary

In an integer constant expression (ICE) in 6.6p6, if an operand is NOT
evaluated, must it follow the constraints and semantics of 6.6?

WG14 messages 14092 to 14102 (with subject of: Fixed size array or VLA?) discuss
this issue.

Places where expressions are not evaluated:

* `0 && funny`
* `1 || funny`
* `0 ? funny : other`
* `1 ? other : funny`
* `_Generic(funny,...)`
* `sizeof(funny)`
* `_Alignof(funny)`

Examples of 'funny' code (that are allowed in expressions that are not
evaluated):

* `assignment = operator`
* `inc++ and ++inc`
* `dec-- and --dec`
* `func_call()`
* `(comma,operator)`
* `3.0`
* `0/0`
* `1.0/0.0`

Places where ICEs are used:

* size of bit-fields, eg, `struct s1{ int bit : ICE; }s2;`
* enum constant, eg, `enum e1{a=ICE}e2;`
* size of non-VLA arrays, eg, `static int ary[ICE];`
* conditional inclusion, eg, `#if ICE`
* null pointer constant, eg, `#define NULL ICE`
* alignment specifier, eg, `_Alignas(ICE)`
* initialization, eg, `{[ICE] = value}`
* static assertions, eg, `_Static_assert(ICE,"string");`
* **case** labels, eg, `case ICE:`
* some object-like macros, eg, `#define EDOM ICE`

Several people expressed an opinion that just parsing the expression (syntax)
without depending upon any values (semantics) is a good thing. However,
**sizeof**(var) depends upon var being a fixed size array versus VLA to
determine if it is a valid ICE. So, some semantic checking must be done.

Some parts of the C standard that might help answer the question follow.

Footnote 118 in 6.6p11 shows the use of 'funny' code:

> ```c
> static int i = 2 || 1 / 0;
> ```

6.6p2:

> A constant expression can be evaluated during translation rather than runtime,
> and accordingly may be used in any place that a constant may be.

6.4.6p2 has:

> An operand is an entity on which an operator acts.

Seems to me that if an operand is not evaluated, then nothing is being acted
upon, so is not an operand.

By 6.6p10

> An implementation may accept other forms of constant expressions.

any implementation may accept these unevaluated expressions; but that does not
mean that all implementations must accept them. And, by the committee discussion
in DR 312 against C99, these "other forms" cannot be an ICE (those words are not
in C99 or C11).

3.1 **access** note 3:

> Expressions that are not evaluated do not access objects.

### Suggested Technical Corrigendum

Add (something along the lines of) either

* (that are evaluated)
* (even if not evaluated)

after "operands" in the first line of 6.6p6 and second line in 6.6p8.

Perhaps, add a footnote giving an example to the phrase being added.

Add to the end of 6.6p10:

> however, they are not integer constant expressions.

Also, update J.2 items on ICE and arithmetic constant expression.
