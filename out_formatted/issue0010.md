## Issue 0010: Is the typedef to an incomplete type valid?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Michael S. Ball, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-044  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_010.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_010.html)

Consider:

```c
typedef int table[];        /* line 1 */

 table one = {1};        /* line 2 */

 table two = {1, 2};     /* line 3 */
```

First, is the typedef to an incomplete type legal? I can't find a prohibition in
the standard. But an incomplete type is completed by a later definition, such as
line 2, so what is the status of line 3?

The type, of which `table` is only a synonym, can't be completed by line 2 if it
is to be used in line 3\. And what is `sizeof(table)`? What old C compilers seem
to do is treat the typedef as some sort of textual equivalent, which is clearly
wrong.

---

Comment from WG14 on 1997-09-23:

### Response

A typedef of an incomplete type is permitted.

Regarding objects `one` and `two`, refer to the standard subclause 6.1.2.5, page
24, lines 8-9: “An array of unknown size is an incomplete type. It is completed,
*for an identifier of that type,* by specifying the size in a later declaration
...” \[emphasis added\]. The types of objects `one` and `two` are completed but
the type `table` itself is *never* completed. Hence, `sizeof(table)` is not
permitted.

An example very similar to that submitted is shown in example 6, subclause 6.5.7
on page 74, lines 16-23.
