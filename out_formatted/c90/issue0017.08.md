## Issue 0017.08: What types are compatible with pointer to `void`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Compatibility of pointer to `void` with storage class

Refer to subclause 6.3.9, page 49, lines 24-25. Do these lines make the
following legal?

```c
register void *p;
 char *q;
 if (p==q)  /* legal */
 ...
```

The wording on line 25, “... version of `void`; or” does not talk about the
“`void` type.” This sentence could be taken as simply referring to the
occurrence of a qualified or unqualified occurrence of `void`.

Should the wording on line 25 be changed to “... version of the type `void`; or”
and thus cause the storage class to be ignored, or does the above example fall
outside the scope of the constraint?

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citation is subclause 6.3.9:

> one operand is a pointer to an object or incomplete type and the other is a
> pointer to a qualified or unqualified version of `void`; or

The Committee believes that the current wording of the standard is clear, and it
is not changed in meaning by changing “version of `void`” in the quoted section
to “version of the `void` type.”

The standard uses the word “`void`” in two contexts: the keyword itself and the
type that the keyword names. The context that the word is used in adequately
distinguishes between the two. In the section quoted, which discusses type
compatibility, a misreading of “`void`” as meaning the keyword quickly results
in nonsense.

As to the qualification discussed in the quoted passage, it is type
qualification, defined in subclause 6.5.3. The standard only uses the words
“qualified” and “unqualified” when discussing type qualification and never uses
them when discussing storage classes. Thus, storage classes have no place in the
discussion of the quoted passage.
