## Issue 0132: Can undefined behavior occur at translation time, or only at run time?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Cross-references: [0019](../c90/issue0019.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_132.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_132.html)

Can undefined behavior occur at translation time, or only at run time? If the
former, then how does one distinguish the two cases in the C Standard?

Consider the translation unit:

```c
/* No headers included */
 int checkup()
        {
        /* Case 1 */
        if (0)
                printf("Printing.\n");
        /* Case 2 */
        return 2 || 1 / 0;
        }
```

Case 1 calls a function with a variable number of arguments without a prototype
in scope. But the call is never actually executed. Now, subclause 6.3.2.2, in
the first paragraph of page 41, states that this is undefined. Is it undefined
to *translate* the code, or to *execute* it? The definition of undefined
behavior (subclause 3.16) clearly allows the former, and subclause 5.3.2.2 does
*not* say that the undefined behavior occurs only if the call is actually
executed.

On the other hand, while subclause 6.3.5 uses similar wording about division by
zero, “we all know” that my Case 2 is strictly conforming.

So what is the answer? If undefined behavior cannot occur at translation time,
why the wording in subclause 3.16? If it can, how do I distinguish the
possibilities? And, by the way, what is the answer for my Case 1?

---

Comment from WG14 on 1997-09-23:

### Response

The Response to [Defect Report #109](../c90/issue0019.md) addresses this issue. The
translation unit must be successfully translated.
