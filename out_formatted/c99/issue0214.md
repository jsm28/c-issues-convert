## Issue 0214: `atexit` function registration

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive Feather (UK)  
Date: 2000-04-04  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_214.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_214.htm)

### Summary

7.20.4.2 reads:

> \[#3\] The implementation shall support the registration of at least 32
> functions.

This does not require registration of a valid function to succeed. The
implementation could fail the first 420 times `atexit()` is called, and then
succeed 32 times. It also does not require `atexit()` to accept any function of
the correct type; theoretically an implementation could reject (say) a function
in a different translation unit.

### Suggested Technical Corrigendum

Change the cited wording to:

> \[#3\] The implementation shall not reject the registration of a valid function
> if less than 32 functions are already registered (multiple registrations of the
> same function counting multiple times).

or add the following words:

> If less than this number are already registered, a call with a valid argument
> shall succeed.

---

Comment from WG14 on 2001-09-18:

### Committee Response

There are many conditions under which any library function or language feature
may fail or behave in an undefined manner. Some examples:

* All of memory has been allocated
* The stack has overflowed

As such, it is a quality of implementation issue under what conditions any
library function, including `atexit()`, may fail.

There is no consensus to make the suggested change or any change along this
line.
