## Issue 0205: New keyword `__at_least`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Canada C Working Group, Raymond Mak (Canada C Working Group)  
Date: 1999-09-15  
Reference document: [ISO/IEC WG14 N893](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n893.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_205.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_205.htm)

### Summary

6.7.5 introduces a new use of the `static` keyword. A new keyword should be used
instead.

This use of `static` can only occur in function parameter declaration. If we
examine the syntax carefully, `static assignment-expression` taken together
inside `[` and `]` really plays the role of a type qualifier qualifying a
pointer. This means the `assignment-expression` should only be allowed to follow
immediately after the keyword `static` (when `static` is present), with no other
type qualifiers allowed in between. Also, a new keyword should be used to make
the meaning clear.

### Suggested Correction

Use a new keyword, `__at_least`, in place of `static`.

Change 6.4.1p1 to add a new keyword: `__at_least`

Change the syntax under 6.7.5 to (the two occurrences of `static` to
`__at_least`):

> *direct\_declarator* `:`  
> *identifier*  
> `(` *declarator* `)`  
> *direct-declarator* `[` *type-qualifier-list<sub>opt</sub>
> assignment-expression<sub>opt</sub>* `]`  
> *direct-declarator* `[ __at_least` *assignment-expression
> type-qualifier-list<sub>opt</sub>* `]`  
> *direct-declarator* `[` *type-qualifier-list<sub>opt</sub>* `__at_least`
> *assignment-expression* `]`  
> ... (the rest is the same as in the FDIS) ...

Change 6.7.5.2p1 to (i.e. the two occurrences of `static` to `__at_least`):

> \[#1\] In addition to optional type qualifiers and the keyword `__at_least`, the
> `[` and `]` may delimit an expression or `*`. If they delimit an expression
> (which specifies the size of an array), the expression shall have an integer
> type. If the expression is a constant expression, it shall have a value greater
> than zero. The element type shall not be an incomplete or function type. The
> optional type qualifiers and the keyword `__at_least` shall appear only in a
> declaration of a function parameter with an array type, and then only in the
> outermost array type derivation.

Change 6.7.5.2p3 to (i.e. the three occurrences of `static` to `__at_least`, and
bind `__at_least` with `assignment-expr` in the syntax):

> > `D[` *type-qualifier-list<sub>opt</sub> assignment-expr<sub>opt</sub>* `]`  
> > `D[ __at_least` *assignment-expr type-qualifier-list<sub>opt</sub>* `]`  
> > `D[` *type-qualifier-list* `__at_least` *assignment-expr* `]`  
> > `D[` *type-qualifier-list<sub>opt</sub>* `* ]`
>
> and the type specified for *ident* in the declaration "`T D`" is
> "*derived-declarator-type-list T*", then the type specified for ident is
> "*derived-declarator-type-list array of T*".<sup>121\)</sup> (See 6.7.5.3 for
> the meaning of the optional type qualifiers and the keyword `__at_least`.)

Change 6.7.5.3p7 to (i.e. `static` to `__at_least`):

> \[#7\] A declaration of a parameter as "array of *type*" shall be adjusted to
> "qualified pointer to *type*", where the type qualifiers (if any) are those
> specified within the `[` and `]` of the array type derivation. If the keyword
> `__at_least` ...

Change 6.7.5.3p21 to (i.e. `static` to `__at_least`):

> \[#21\] EXAMPLE 5 The following are all compatible function prototype
> declarators.
>
> ```c
>        double maximum(int n, int m, double a[n][m]);
>         double maximum(int n, int m, double a[*][*]);
>         double maximum(int n, int m, double a[ ][*]);
>         double maximum(int n, int m, double a[ ][m]);
> ```
>
> as are:
>
> ```c
>        void f(double (* restrict a)[5]);
>         void f(double a[restrict][5]);
>         void f(double a[restrict 3][5]);
>         void f(double a[restrict __at_least 3][5]);
>         ...
> ```

Change A.1.2 to add keyword:

> ```c
> __at_least
> ```

**Explanation of the change**  
The new syntax groups '`__at_least` *assignment-expression*' together. For
example:

> `double a[restrict __at_least 3] /*` *ok* `*/`  
> `double a[__at_least 3 restrict] /*` *ok* `*/`  
> `double a[__at_least restrict 3] /*`*not ok* `*/`

Conceptually, '`__at_least` *assignment-expression*' is a type qualifier. Even
though we do not treat it as such in C9X, the potential is there for future
enhancement of the language. Therefore we should not interfere with possible
future changes in this respect. The following example illustrates the point.

In a function parameter declaration, a parameter of "array of *type*" is
adjusted to "qualified pointer to *type*". The type-qualifiers inside `[` and
`]` become the qualifier for the pointer. If
'`__at_least`*assignment-expression*' is also a type qualifier, this adjustment
enables us to write:

> ```c
> int * __at_least(10) p;
> ```

which declares a pointer pointing to the first of a sequence of 10 integers in
memory. (The parentheses are used for clarity.) The clumsy description in
6.7.5.3p7 become unnecessary. Note that the current `static` syntax prevents us
from writing the equivalent pointer declaration for an array parameter
declaration.

This example is presented here only as an illustration of what is possible in
the future; it is not meant as a suggested change for this DR. Nevertheless, it
does show that allowing other qualifiers appearing between `static` and the
*assignment-expression* is a conceptual error.

---

Comment from WG14 on 2001-09-18:

### Committee Discussion

The committee has had several viewpoints on this controversial item. These are
ranked with the choice getting the most support first, the last entry getting
little or no support.

1. Do nothing.
2. Remove this feature (the use of **static** to mean a minimum array size).
3. Deprecate this feature (the use of **static** to mean a minimum array size).
4. In 6.7.5 Declarators (p. 114\) and its subclauses, deprecate:
   > *direct-declarator* `[ static` *type-qualifier-list<sub>opt</sub>
   > assignment-expression* `]`

   and change:
   > *direct-declarator* `[` *type-qualifier-list* `static` *assignment-expression*
   > `]`

   to:
   > *direct-declarator* `[` *type-qualifier-list<sub>opt</sub>* `static`
   > *assignment-expression* `]`
5. Accept the suggestions of this DR.

> *<ins>Note:</ins>*
>
> > There was a unanimous vote that the feature is *ugly*, and a good consensus that
> > its incorporation into the standard at the 11<sup>th</sup> hour was an
> > unfortunate decision.

---

Comment from WG14 on 2001-09-18:

### Committee Response

There is no consensus to make this change or any change along this line.
