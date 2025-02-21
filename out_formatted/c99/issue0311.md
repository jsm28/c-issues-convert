## Issue 0311: Definition of variably modified types

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Joseph Myers \<joseph@codesourcery.com\>, UK C Panel  
Date: 2005-03-04  
Reference document: [ISO/IEC WG14 N1099](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1099.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_311.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_311.htm)

### Summary

Variably modified types are defined by 6.7.5#3:

> \[#3\] A *full declarator* is a declarator that is not part of another
> declarator. The end of a full declarator is a sequence point. If the nested
> sequence of declarators in a full declarator contains a variable length array
> type, the type specified by the full declarator is said to be *variably
> modified*.

It is desirable for the definition to look at the declarator rather than just
the resulting type, so that function parameters adjusted from array to pointer
type are variably modified if the array size is variable: in

```c
    void
    f (int i, int a[static ++i])
    {
      // ...
    }
```

the increment of `i` must be evaluated for the definition of `static` in this
context to make sense. However, what it means for the declarators to "contain" a
type is unclear. The natural interpretation is that they include an array
declarator with array size `[*]` or an expression which is not an integer
constant expression. However, this does not cover cases such as

```c
    int x;
    // ...
    typedef int vla[x];
    vla y[3];
```

where a typedef for a variably modified type is used. `y` is a VLA, and clearly
ought to be variably modified, but nothing about the declarators makes it
variably modified; only the declaration specifier does so.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2007-09-06:

### Committee Discussion (for history only)

Declarators don't contain a type, it is the sequence of declarators that
contains types.

The sentence in 6.7.5;p3 that defines variably modified types may be wrong, and
that may not even be the right place for it to be defined. The definition ties
it too closely to the declarator. In the example provided in the DR, the type of
`y` is variably modified. The declarator for `y` does not include a variable
length array type. Para 3 needs to have it's wording adjusted in some fashion,
the text there is insufficient to provide us the answer.

The definition in the standard for variable length array does not seem to be in
italics.

2006-Mar-29:

For the reason noted in the Summary, variably modified types do need to be tied
to the declarator syntax.  But the current definition fails to state that a new
type derived from a variably modified type is itself variably modified.

### Committee Response

Yes, this is a defect in the definition..  The definition will be modified to
state explicitly that types derived from a variably modified type are themselves
variably modified.

### Technical Corrigendum

\[**Note**, these are relative to wg14's
[N1124](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1124.pdf).\]

Change 3rd sentence in 6.7.5p3 from:

> If the nested sequence of declarators in a full declarator contains a variable
> length array type, the type specified by the full declarator is said to be
> *variably modified*.

to

> If in the nested sequence of declarators in a full declarator there is a
> declarator specifying a variable length array type, the type specified by the
> full declarator is said to be *variably modified*.  Furthermore, any type
> derived by declarator type derivation from a variably modified type is itself
> variably modified.
