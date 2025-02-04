## Issue 0457: The `ctime_s` function in Annex K defined incorrectly

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, David Keaton (suggested by Jens Gustedt)  
Date: 2014-03-13  
Reference document: [N1802](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1802.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The `ctime_s` function in Annex K was defined analogously to `ctime`, and some
of the text from the definition of `ctime` was copied and modified slightly.

K.3.8.2.2p4 states that `ctime_s` is equivalent to the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

In this case, the text from the original `ctime` definition was not quite
modified enough.  The `localtime_s` function takes two arguments and the above
code only supplies one.

### Suggested Technical Corrigendum

In K.3.8.2.2p4, replace

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

with the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer, &(struct tm){ 0 }))
> ```

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Proposed Technical Corrigendum

In K.3.8.2.2p4, replace

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

with the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer, &(struct tm){ 0 }))
> ```
