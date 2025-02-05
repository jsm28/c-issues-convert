## Issue 0158: Are the semantics for the explicit conversion of null pointer constants defined?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Cross-references: [0155](issue0155.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_158.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_158.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com.*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 006: Null pointer conversions

The C Standard does not define semantics for the explicit conversion of null
pointer constants and for the implicit conversion of null pointers.

Subclause 6.2.2.3 reads in part:

If a null pointer constant is assigned to or compared for equality to a pointer,
the constant is converted to a pointer of that type. Such a pointer, called a
null pointer, is guaranteed to compare unequal to a pointer to any object or
function.

Two null pointers, converted through possibly different sequences of casts to
pointer types, shall compare equal.

Given the definitions:

```c
void * p = 0;
 int  * i = 0;
```

does the standard guarantee that the expression `p == i` always evaluates to 1?
The last quoted sentence only covers casts, and not the implicit conversions of
that comparison. Conversely, do the expressions `(int *)0` or `1 ? 0 : (int *)0`
yield null pointers of type `(int *)`? The quoted text does not cover the case
of a null pointer constant being converted other than by assignment or in a test
for equality, yet expressions such as these are widely used.

### Suggested Technical Corrigendum:

In subclause 6.2.2.3, change:

> Two null pointers, converted through possibly different sequences of casts to
> pointer types, shall compare equal.

to:

> Conversion of a null pointer to another pointer type yields a null pointer of
> that type. Any two null pointers shall compare equal.

Alternatively, a common term could be introduced to more conveniently describe
the various forms of pointer that cannot be dereferenced. In this case, replace
the last two paragraphs of subclause 6.2.2.3 with:

> For each pointer type, there exist values which can participate in assignment
> and equality operations, but which cause undefined behavior if dereferenced.
> These are referred to as *undereferenceable.* An undereferenceable pointer
> compares unequal to any other value of the same pointer type. For each pointer
> type, one particular undereferenceable pointer value is called the *null
> pointer.* \[Footnote: Since there is only one such value, all null pointers of
> the same type compare equal.\]
>
> An integral constant expression with the value 0, or such an expression cast to
> type `void *`, is called a *null pointer constant.* If a null pointer constant
> is assigned to or compared for equality with an object of pointer type, or cast
> to pointer type, then it is converted to the null pointer of that type.
> Conversion of a null pointer to another pointer type produces the null pointer
> of that type.

If the answer to [Defect Report #155](issue0155.md) is that *unique* means
*different each time,* then replace the last two sentences of subclause 7.10.3
with:

> If the size of the space requested is zero, an undereferenceable pointer is
> returned. It is implementation-defined whether this is always a null pointer or
> whether the implementation attempts to produce a value distinct from any other
> undereferenceable pointer. Any pointer value returned by an allocation can be
> passed to the free function; if the value is not a null pointer, it becomes
> indeterminate. \[Footnote: A subsequent allocation may return a pointer value
> with the same bit pattern, but a strictly conforming program can't detect
> this.\] The value of a pointer that refers to any part of a freed object is also
> indeterminate.

---

Comment from WG14 on 1997-09-23:

### Response

Does the Standard guarantee that `p == i`? Yes.

Does `(int *) 0` yield a null pointer of type `int *`? Yes.

Does `1 ? 0 : (int *) 0` yield a null pointer of type `int *`? Yes.

The intent of the part of Subclause 6.2.2.3 that you quote is to state that a
null pointer results when a null pointer constant is converted to a pointer. By
singling out assignment and comparison, the Standard is misleadingly specific.
This should be clarified in the Standard.

### Future Change

In Subclause 6.2.2.3

Change

> "If a null pointer constant is assigned to or compared for equality to a
> pointer, the constant is converted to a pointer of that type. Such a pointer,
> called a null pointer, is guaranteed to compare unequal to a pointer to any
> object or function.
>
> Two null pointers, converted through possibly different sequences of casts to
> pointer types, shall compare equal."

To

> "The result of converting a null pointer constant to a pointer type is called a
> null pointer. A null pointer is guaranteed to compare unequal to a pointer to
> any object or function.
>
> Conversion of a null pointer to another pointer type yields a null pointer of
> that type. Any two null pointers shall compare equal."

In Subclause 6.3.9

Add a new paragraph after the first paragraph in Semantics

> "If a null pointer constant is compared for equality to a pointer, the constant
> is converted to the type of the pointer."
