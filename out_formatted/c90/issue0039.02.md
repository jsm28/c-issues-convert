## Issue 0039.02: Should `setlocale(LC_ALL, NULL)` return `"C"` in the `"C"` locale?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Vania Joloboff, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-061  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_039.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_039.html)

I also would like to make a requirement that if the current locale is the `"C"`
locale, the value returned by `setlocale(LC_ALL, NULL)` be a string of length
one, consisting of the single character `C`.

Currently the value of `setlocale(LC_ALL, NULL)` is unspecified for the `"C"`
locale.

This makes it difficult to build libraries where you want to maintain the
behavior pre-existing to internationalization for backward compatibility.

Typically you want to say in these programs:

```c
if (*setlocale(LC_ALL, NULL) == 'C')
 do the old thing
 else
 do the new thing
```

---

Comment from WG14 on 1997-09-23:

### Response

The reference is to subclause 7.4.1.1, page 107\.

The Committee acknowledges that there exists no strictly portable method for
determining whether the current locale is the `"C"` locale. The request for this
feature is neither an erratum nor a request for interpretation; it is a request
for an amendment. The Committee will consider this request for a future revision
of the C Standard.
