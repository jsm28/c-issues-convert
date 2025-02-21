## Issue 0068: When are values of the type `char` treated as `signed`or `nonnegative` integers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_068.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_068.html)

Item 5 \- handling of `char` values

Values of the type `char` must be treated as either “signed” or “nonnegative”
integers (subclause 6.1.2.5).

a. Is the treatment determined strictly by the value of the expression `CHAR_MAX
== SCHAR_MAX`?

b. If the treatment is as “signed” integers, does the type `char` behave in
every instance as the type `signed char` (though of course being a different
type)? If not, what are the differences?

c. If the treatment is as “nonnegative” integers, does the type `char` behave in
every instance as the type `unsigned char` (though of course being a different
type)? If not, what are the differences? In particular, do the "no overflow,
reduce modulo" semantics apply?

---

Comment from WG14 on 1997-09-23:

### Response

a) Yes.

b) and c) Yes. Subclause 6.2.1.1, “As discussed earlier, ...” indicates that
this is the intent.
