## Issue 0499: Anonymous structure in union behavior

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Rajan Bhakta  
Date: 2016-04-12  
Reference document: [N2038](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2038.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C23  
Cross-references: [0502](issue0502.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

```c
Given the following code:

union U {
  struct {
    char B1;
    char B2;
    char B3;
    char B4;
  };
  int word;
} u;

Does the storage of B1, B2, B3 and B4 overlap?

According to 6.7.2.1#13, the members should overlap in storage as they become members of 'union U'.
At least one implementation (GCC) seems to NOT consider them to be overlapping.
At least one implementation (IBM's XL LE AIX) considers them to be overlapping as the standard currently states.

Similar code present in example 1 on 6.7.2.1#19.

Suggested TC:
  If the intent is that the members do NOT overlap:
    Append to 6.7.2.1#13:
      Anonymous structures maintain the structure type if they are considered to be members of the containing union.*)
      *) This means the structure members are not considered to occupy the same storage as if they were directly union members.
  If the intent is that the members DO overlap:
    No change, or perhaps add on a comment to 6.7.2.1#19 Example 1:
    ...
    struct { int i, j; }; // anonymous structure, i and j now overlap in storage
    ...
```

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

> The storage does not overlap.
>
> A related issue is to be found in [DR 502](issue0502.md) and both may be resolved
> with coordinated wording changes.

Apr 2017 meeting

### Committee Discussion

> The committee briefly discussed [(SC22WG14.14628) My approach to DR 499 and
> 502](https://www.open-std.org/jtc1/sc22/wg14/14628) which argues that this might
> be simply an editorial issue, such that a change as simple as:
>
> Change §6.7.2.1 p13 from:
>
> > An unnamed member of structure type with no tag is called an *anonymous
> > structure*; an unnamed member of union type with no tag is called an *anonymous
> > union*. The members of an anonymous structure or union are considered to be
> > members of the containing structure or union. This applies recursively if the
> > containing structure or union is also anonymous.
>
> to:
>
> > An unnamed member of structure type with no tag is called an *anonymous
> > structure*; an unnamed member of union type with no tag is called an *anonymous
> > union*. The names of members of an anonymous structure or union are added to the
> > name space of the containing structure or union. This applies recursively if the
> > containing structure or union is also anonymous.
>
> would adequately resolve the issue.

Oct 2017 meeting

### Committee Discussion

> The suggestion almost works but not quite, as discussed in [(SC22WG14.14632) My
> approach to DR 499 and 502,](https://www.open-std.org/jtc1/sc22/wg14/14632)
> where a flexible array member following an anonymous structure would no longer
> be allowed.
>
> Further thought is needed.

Apr 2018 meeting

### Committee Discussion

> A short paper was solicited, discussed, and adopted as the Proposed Change to a
> new revision of the Standard.
>
> It was noted that additional wording might be appropriate with regard to both
> tail padding and to address flexible array members.

### Proposed Change

Change §6.7.2.1 p13 from:

> An unnamed member of structure type with no tag is called an *anonymous
> structure*; an unnamed member of union type with no tag is called an *anonymous
> union*. The members of an anonymous structure or union are considered to be
> members of the containing structure or union. This applies recursively if the
> containing structure or union is also anonymous.

to:

> An unnamed member of structure type with no tag is called an *anonymous
> structure*; an unnamed member of union type with no tag is called an *anonymous
> union*. The members of an anonymous structure or union are considered to be
> members of the containing structure or union, keeping their structure or union
> layout. This applies recursively if the containing structure or union is also
> anonymous.
