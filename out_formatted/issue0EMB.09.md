## Issue 0EMB.09: Effective type definition (aka US-40)

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [184](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/184), [195](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/195), [199](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/199), [207](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/207)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Description: a couple of the statements concerning effective types in 6.5 of the
C Standard are not exactly correct in the presence of address-space qualifiers.
The easiest fix is probably to modify the concept of *effective type* in the C
Standard so as not to include an address-space qualifier. (The whole concept of
*effective type* is used only in 6.5 and in one footnote elsewhere in the C
Standard.)

Possible solution: add the following section to clause 5.3 of TR 18037:

> **Clause 6.5 \- Expressions**, replace the first two sentences of paragraph 6
> with: The *effective type* of an object for an access to its stored value is the
> declared type of the object, if any, without any address-space qualifier that
> the declared type may have.<sup>72\)</sup> If a value is stored into an object
> having no declared type through an lvalue having a type that is not a character
> type, then the type of the lvalue, without any address-space qualifier, becomes
> the effective type of the object for that access and for subsequent accesses
> that do not modify the stored value.

and remove the notion *additionally access-qualified version* from TR 18037
(first replacement paragraph of paragraph 26 of 6.2.5, replacement text for
paragraph 7 of 6.5).

---

Comment from WG14 on 2004-11-15:

Problem: If \_X and \_Y are address spaces with \_Y enclosing \_X, after the
declarations

```c
_X char a;


_Y char *p = &a;
```

the dereference \*p is undefined because of the way TR 18037 applies the notion
of effective type (C Standard 6.5, paragraphs 6 and 7). This makes overlapping
named address spaces unusable by strictly conforming code in most circumstances.

Solution: In the detailed changes to the C Standard, modify the definition of
*effective type* (clause 6.5, paragraph 6\) to exclude address space qualifiers,
and restore the rules in paragraph 7 to their original form. (Note that the
whole concept of *effective type* is used only in 6.5 and in one footnote
elsewhere in the C Standard.) This makes TR 18037's definition of *additionally
access-qualified version* of a type (in the new text for 6.2.5) unnecessary.

Changes: Change the replacement text for clause 6.5 of the C Standard to the
following:

> **Clause 6.5 \- Expressions**, replace the first two sentences of paragraph 6
> with:
>
> The *effective type* of an object for an access to its stored value is the
> declared type of the object, if any, without any address-space qualifier that
> the declared type may have.<sup>72\)</sup> If a value is stored into an object
> having no declared type through an lvalue having a type that is not a character
> type, then the type of the lvalue, without any address-space qualifier, becomes
> the effective type of the object for that access and for subsequent accesses
> that do not modify the stored value.

Remove the sentence defining *additionally access-qualified version* from TR
18037 (first paragraph replacing paragraph 26 of 6.2.5).
