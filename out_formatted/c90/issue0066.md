## Issue 0066: A set of locale questions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_066.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_066.html)

Item 3 \- locales

In a conforming implementation, can the value of any of the following
expressions (subclause 7.4.2.1) be a value other than 0 or 1? Can the value of
the first expression be 0?

> ```c
> strlen(localeconv()->decimal_point)
>         strlen(localeconv()->thousands_sep)
>         strlen(localeconv()->mon_decimal_point)
>         strlen(localeconv()->mon_thousands_sep)
> ```

If the value can be greater than 1, can the string contain more than one
multibyte character? If so, can the string contain shift sequences? If so, can
the string end other than in the initial shift state?

---

Comment from WG14 on 1997-09-23:

### Response

Of the four `strlen` calls, the first must return 1, the second must return 0 or
1, and the other two must return 0 or more, in a conforming implementation.
There is a specific requirement for `decimal_point` in the second paragraph of
subclause 7.4.2.1 **Description**, and in the individual descriptions
“character” is intended to imply 0 or 1 while “string” is meant to imply 0 or
more.
