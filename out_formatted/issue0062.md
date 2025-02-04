## Issue 0062: Can the `rename` function alway return a failure?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: David J. Hendricksen, X3 Secretariat (USA)  
Date: 1993-08-19  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_062.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_062.html)

If the only way to effectuate the renaming of a file on a given system is to
copy the contents of the file, does an implementation conform to the C Standard
by always returning a failure from the `rename` function? Footnote 113 would
seem to imply this.

---

Comment from WG14 on 1997-09-23:

### Response

Yes, subclause 7.9.4.2 permits the `rename` function to fail if it must copy the
file contents, among other reasons.
