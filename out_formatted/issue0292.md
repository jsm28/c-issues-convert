## Issue 0292: Use of the word *variable*

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Convener, J. Benito (convener)  
Date: 2003-09-18  
Reference document: [ISO/IEC WG14 N1025](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1025.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_292.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_292.htm)

### Summary

Change the use of *variable* to *object* in those instances where the Standard
is referring to an object.

### Suggested Technical Corrigendum

*EXAMPLE 2, 5.1.2.3*, change

> the value of each variable to size `int`

to

> the value of each object to size `int`

*Footnote 41*, change

> Thus, an automatic variable can be initialized to a trap representation without
> causing undefined behavior, but the value of the variable cannot be used until a
> proper value is stored in it.

to

> Thus, an automatic object can be initialized to a trap representation without
> causing undefined behavior, but the value of the object cannot be used until a
> proper value is stored in it.

*EXAMPLE 1, 6.5.16.1*, change

> Therefore, for full portability, the variable `c` should be declared as `int`.

to

> Therefore, for full portability, the object `c` should be declared as `int`.

*EXAMPLE, 6.7.5.1*, change

> EXAMPLE The following pair of declarations demonstrates the difference between a
> “variable pointer to a constant value” and a “constant pointer to a variable
> value”.

to

> EXAMPLE The following pair of declarations demonstrates the difference between a
> “object pointer to a constant value” and a “constant pointer to a object value”.

*6.8.5.3 #1*, change

> If *clause-1* is a declaration, the scope of any variables it declares is the
> remainder of the declaration and the entire loop, including the other two
> expressions;

to

> If *clause-1* is a declaration, the scope of any objects it declares is the
> remainder of the declaration and the entire loop, including the other two
> expressions;

*Footnote 134*, change

> Thus, *clause-1* specifies initialization for the loop, possibly declaring one
> or more variables for use in the loop;

to

> Thus, *clause-1* specifies initialization for the loop, possibly declaring one
> or more objects for use in the loop;

*Footnote 165*, change

> For a variable `z` of complex type, `z == creal(z) + cimag(z)*I`.

to

> For the object `z` of complex type, `z == creal(z) + cimag(z)*I`.

*Footnote 166*, change

> For a variable `z` of complex type, `z == creal(z) + cimag(z)*I`.

to

> For the object `z` of complex type, `z == creal(z) + cimag(z)*I`.

*7.6, #1,* change

> A floating-point status flag is a system variable whose value is set (but never
> cleared) when a floating-point exception is raised,

to

> A floating-point status flag is a system object whose value is set (but never
> cleared) when a floating-point exception is raised,

*7.6, #1,* change

> A floating-point control mode is a system variable whose value may be set by the
> user to affect the subsequent behavior of floating-point arithmetic.

to

> A floating-point control mode is a system object whose value may be set by the
> user to affect the subsequent behavior of floating-point arithmetic.

*F.8.1,* change

> The flags and modes in the floating-point environment may be regarded as global
> variables;

to

> The flags and modes in the floating-point environment may be regarded as global
> objects;

*Footnote 308*, change

> Use of `float_t` and `double_t` variables increases the likelihood of
> translation-time computation.

to

> Use of `float_t` and `double_t` objects increases the likelihood of
> translation-time computation.

Annex I #2, bullet 11, change

> or an enumeration variable that has the same type

to

> or an enumeration object that has the same type

---

Comment from WG14 on 2006-04-04:

### Committee Discussion

1. No change needed.
2. Sec 6.2.6.1 variable is common usage \- no change needed.
3. No change needed.
4. No change needed.
5. Change *variable* to *identifiers*.
6. No change needed.
7. No change needed.
8. No change needed.
9. No change needed.
10. No change needed.
11. No change needed.
12. No change needed.
13. No change needed.
14. Agree with suggested change.

### Technical Corrigendum

*6.8.5.3 #1*, change

> If clause-1 is a declaration, the scope of any variables it declares is the
> remainder of the declaration and the entire loop, including the other two
> expressions;

to

> If clause-1 is a declaration, the scope of any identifiers it declares is the
> remainder of the declaration and the entire loop, including the other two
> expressions;

Annex I #2, bullet 11, change

> or an enumeration variable that has the same type

to

> or an enumeration object that has the same type
