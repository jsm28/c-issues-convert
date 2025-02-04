## Issue 0222: Partially initialized structures

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC2  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_222.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_222.htm)

### Summary

Consider the code extract:

```c
   struct listheader
     {
         struct item *head;
         struct item *tail;
     };
     // The following is at block scope    struct listheader h1;
     h1.head = NULL;
     struct listheader h2;
     h2 = h1;
```

The value of `h1.tail` is indeterminate throughout, but provided that the code
never accesses it this is not a problem. However, if it holds a trap
representation, the assignment to `h2` involves assigning a trap representation,
which is undefined behaviour.

There are two possible resolutions I can think of:

1. Say that the code is defined. Any implementation that uses memberwise copying of structures now has to explicitly disable detection of trap values.
2. Say that the code is undefined. This is going to surprise a number of people. In particular, it becomes impossible to assign any structure where the complete list of fields is unknown (e.g. any structure defined in a Standard header).

---

Comment from WG14 on 2001-09-18:

### Committee Discussion (for history only)

A TC should remove the notion of objects of struct or union type having a trap
representation. Changes need to be made to 6.2.6.1 paragraphs 6 and 7, and
footnote 42\. It was observed that the point of the original footnote was
primarily to illustrate one reason why padding bits might not be copied: because
member-by-member assignment might be performed. But member-by-member assignment
would imply that struct assignment could produce undefined behavior if a member
of the struct had a value that was a trap representation. Instead of adding
further text explaining that member values that were trap representations were
not permitted to render assignment of a containing struct or union object
undefined (e.g. if member-by-member copying were used), it was decided that the
footnote should simply clarify the issue of padding bits directly.

---

Comment from WG14 on 2001-09-18:

### Technical Corrigendum

Change 6.2.6.1 paragraph #6 to:

> When a value is stored in an object of structure or union type, including in a
> member object, the bytes of the object representation that correspond to any
> padding bytes take unspecified value.<sup>42\)</sup> The value of a struct or
> union object is never a trap representation, even though the value of a member
> of a struct or union object may be a trap representation.

Change footnote 42 to:

> 42\) Thus, for example, structure assignment need not copy any padding bits.

Change 6.2.6.1 paragraph #7 to:

> When a value is stored in a member of an object of union type, the bytes of the
> object representation that do not correspond to that member but do correspond to
> other members take unspecified values.
