## Issue 0136: Does `mktime` yield a -1 in the *spring-forward* gap when `tm_isdst` is -1?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Paul Eggert, Project Editor (P.J. Plauger)  
Date: 1994-03-31  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_136.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_136.html)

Suppose I run the following program in a US environment, where the clocks will
jump forward from 01:59:59 to 03:00:00 on April 3, 1994\. This program attempts
to invoke `mktime` on a `struct tm` that represents 02:30:00 on that date. Does
the C Standard let `mktime` return -1 in this case?

```c
#include <stdio.h>
 #include <time.h>
 int main()
        {
        struct tm t;
        time_t r;

        /* 1994-04-03 02:30:00 */
        t.tm_year = 1994 - 1900; t.tm_mon = 3; t.tm_mday = 3;
        t.tm_hour = 2; t.tm_min = 30; t.tm_sec = 0;

        t.tm_isdst = -1; /* i.e. unknown */

        r = mktime(&t);
        if (r == -1)
                printf("mktime failed\n");
        else
                printf("%s", ctime(&r));
        return 0;
        }
```

The ANSI C Rationale (corresponding to subclause 7.12.2.3) clearly lets `mktime`
yield -1 in the “fall-backward fold” that will occur when the clock is turned
back from 01:59:59 to 01:00:00 on October 30, 1994\. The question is whether
`mktime` is also allowed to yield -1 in the “spring-forward gap” when the clock
is advanced from 01:59:59 to 03:00:00.

This question arose when Arthur David Olson's popular “tz” time zone software
was tested using NIST-PCTS:151-2, Version 1.4, (1993-12-03) a test suite put out
by the National Institute of Standards and Technology that attempts to test C
and Posix conformance. The PCTS package insists that in the above case, `mktime`
must yield a `time_t` corresponding to either 01:30:00 or 03:30:00; i.e. PCTS
rejects Olson's `mktime`, which yields -1.

This test case differs in an important way from the common practical use of
`mktime` to “add 1” to the output of `localtime` or `gmtime`, since those
functions normally set `tm_isdst` to a nonnegative value, whereas `tm_isdst` is
-1 in the case under question.

I suggest that the Committee issue a clarification which makes it clear that
`mktime` can yield -1 in the spring-forward gap when `tm_isdst` is -1.

---

Comment from WG14 on 1997-09-23:

### Response

The Standard does not specify the behavior precisely enough to preclude `mktime`
from returning a value of `(time_t)-1` and leaving the `tm_isdst` member set to
-1 in such situations.
