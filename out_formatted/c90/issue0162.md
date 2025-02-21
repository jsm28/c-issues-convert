## Issue 0162: Is the description of the static objects used by `time.h` functions misleading?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_162.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_162.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 010: `gmtime` and `localtime`

The C Standard's description of the static objects used by `time.h` functions is
misleading.

Subclause 7.12.3 reads in part:

these functions return values in one of two static objects: a broken-down time
structure and an array of `char`. Execution of any of the functions may
overwrite the information returned in either of these objects by any of the
other functions.

Does this mean that, for example, `localtime` and `gmtime` must share a single
broken-down time structure, and so the value returned from `gmtime`, if not a
null pointer, must equal the value returned from `localtime` (and this value
cannot change during execution of the program)?

The wording *the other functions* also implies that a call to `gmtime` can
overwrite a previous call to `localtime`, but not a previous call to `gmtime`.
This is clearly ridiculous.

### Suggested Technical Corrigendum

In subclause 7.12.3, change:

these functions return values in one of two static objects: a broken-down time
structure and an array of `char`. Execution of any of the functions may
overwrite the information returned in either of these objects by any of the
other functions.

to:

these functions each return a pointer to an object of static storage duration
after assigning a value to it. Execution of any of these functions may overwrite
the information returned in any of these objects by a previous call to any of
these functions.

---

Comment from WG14 on 1997-09-23:

### Future Change

In subclause 7.12.3, change:

> Except for the `strftime` function, these functions return values in one of two
> static objects: a broken-down time structure and an array of `char`. Execution
> of any of the functions may overwrite the information returned in either of
> these objects by any of the other functions.

to:

> Except for the `strftime` function, these functions each return a pointer to one
> of two types of static objects: a broken-down time structure or an array of
> `char`. Execution of any of the functions that return a pointer to one of these
> object types may overwrite the information in any object of the same type
> pointed to by the value returned from any previous call to any of them.
