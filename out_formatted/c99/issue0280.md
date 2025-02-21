## Issue 0280: `struct tm`, member `tm_isdst`, and `mktime()` in `<time.h>`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Emmanuel Ruffin (ruffin@besancon.sema.slb.com) via ANSI, Randy Meyers (US)  
Date: 2002-09-26  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_280.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_280.htm)

### Summary

If it is not known whether daylight saving time is in effect (`tm_isdst` set to
`-1`), some times expressed in `struct tm` become ambiguous. There is no
specification as to what `mktime()` should do for such cases.

**Questions**

1. Normally when calling `mktime()`, the user will set `tm_isdst` to `-1` to request that `mktime()` determine the true value (See 7.23.2.3 footnote 267). Usually, `mktime()` can determine whether daylight saving time is in effect based on the time and date information initially stored in the `struct tm` argument. However, during the Fall change over, there is one hour that exists both in daylight saving time and standard time. Example: In France, we will change time on October the 27th at 3am. That means that at 3am it will be 2am again. If asked to convert October 27 at 2.30am when `tm_isdst` is `-1`, what value should `mktime()` store in `tm_isdst` and what is the return value?
2. For the same example as point `1`, what should we return in case `tm_isdst` is set to `0` or `1` ?
3. In a general case, what should we do in case `tm_isdst` is different from `-1` ?
4. When calling `mktime()` function, is it true that this function should modify the `tm` structure to put in it the GM time instead the local time given as an entry ?

### Suggested Committee Response

Subclause 7.23.1 Paragraph 1 of the C Standard says,

> "The local time zone and Daylight Saving Time are implementation-defined."

That means that the standard does not specify the behavior and that the
implementation is free to make choices that it must document. Although the C
Standard imposes no particular definition on daylight saving time, other
standards or local custom may.

1. It is implementation defined. For example, an implementation might assume that daylight saving time is not in effect and set `tm_isdst` to `0` and return the `time_t` value corresponding to 2:30 AM Standard Time.
2. It is implementation defined. However, assuming that an implementation chose a conventional definition of daylight saving time, these times are unambiguous since the user specified whether daylight saving time was in effect, and the `time_t` return value would be different for 2:30 daylight saving time versus 2:30 standard time. Note that it would be reasonable for `mktime()` to change `tm_hour` and `tm_isdst` on output. For example, `tm_hour=2` and `tm_isdst=1` on input might change to `tm_hour=1` and `tm_dst=0` on output.
3. It is implementation defined. One possibility would be to consider any two `struct tm` values as being exactly one hour apart if all members have the same value except that one `struct tm` value has `tm_isdst=1` and the other has `tm_isdst=0` (regardless of the date stored in the `struct tm` values).
4. No. A `struct tm` represents a local time in the local time zone for `mktime()`. See 7.23.2.3 Paragraph 2\.

---

Comment from WG14 on 2003-10-06:

### Committee Response

> It is implementation defined. One possibility would be to consider any two
> `struct tm` values as being exactly one hour apart if all members have the same
> value except that one `struct tm` value has `tm_isdst=1` and the other has
> `tm_isdst=0` (regardless of the date stored in the `struct tm` values).
>
> See footnote 267\.
