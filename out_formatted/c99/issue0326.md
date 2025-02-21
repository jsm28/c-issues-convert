## Issue 0326: `asctime()`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: The Austin Group, Stoughton (US)  
Date: 2006-03-28  
Reference document: [AI-053.txt](http://www.opengroup.org/austin/interps/protected/uploads/20/9920/AI-053.txt), [DR 217](../c99/issue0217.md)  
Submitted against: C99  
Status: Fixed  
Fixed in: C11  
Cross-references: [0217](../c99/issue0217.md)  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_326.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_326.htm)

**Summary:** `asctime() tm_year gt 9999`

This is a potential defect forwarded from the Austin Group.

If `asctime()` is called with a tm structure whose `tm_year` field results in a
year \> 9999 (which is possible with 64-bit `time_t`), the current specification
of `asctime()` would result in `asctime()` to overrunning a 26-character buffer;
the specification says the `sprintf()` format for printing the year is "%d", and
(eg) a 5-digit number would print 5 characters, overrunning the buffer.

Similarly, since the user can create the input `struct tm`, it is possible for
the user to set the fields of the `struct tm` to values that are outside the
normal bounds. In such a case, the `sprintf()` format given in the `asctime()`
specification can result in a buffer overrun. For example, if `tm_hour` is
`100`, the `sprintf()` format `.2d` writes the string "100", which could result
in a buffer overrun. The specification should be updated to state the algorithm
can be used as long as the values of the `tm` struct are restricted to the
normal bounds.

### Suggested Technical Corrigendum

Change 7.23.3.1 para 2 from:

> The asctime function converts the broken-down time in the structure pointed to
> by `timeptr` into a string in the form:

To:

> The `asctime()` function shall convert the broken-down time in the structure
> pointed to by `timeptr` into a string in the form, provided the broken-down time
> in the fields of the structure pointed to by `timeptr` contain values that are
> within the normal ranges as defined in `<time.h>`, and the calculated year does
> not exceed four digits:

(NB, see 7.23.1 para 4 for the specifications of the "normal ranges").

Also, add after the example code, and before the "Returns" section, the
following new paragraph:

> Otherwise, if any of the fields of the `tm` structure pointed to by `timeptr`
> contain values that are outside the normal ranges, the behavior of `asctime()`
> is undefined. If the calculated year exceeds four digits, the behavior is
> undefined.

---

Comment from WG14 on 2007-09-06:

### Committee Discussion (for history only)

The proposed resolution invalidates code that strictly conforms to the C99
standard. Here is a contrived example (though there are some examples that are
not contrived):

```c
   #include <time.h>
   #include <stdio.h>

   struct tm tm;

   int
   main (void)
   {
     tm.tm_wday = 0;
     tm.tm_mon = 0;
     tm.tm_mday = -99;
     tm.tm_hour = 99;
     tm.tm_min = 99;
     tm.tm_sec = 99;
     tm.tm_year = -999 - 1900;
     printf ("%s\n", asctime (&tm));
     return 0;
   }
```

This code strictly conforms to C99, with well-defined behavior, and some
implementations prints "Sun Jan-99 99:99:99 -999". The proposed resolution
places extra constraints on asctime's arguments that would cause the above code
to have undefined behavior.

The original interpretation request considered by the Austin Group contained an
additional requirement, that the calculated year should not precede the Epoch
(the date and time associated with `(time_t)0)`. This restriction was removed in
forwarding this to the C committee, since there is no C equivalent concept.
However, if the calculated year is less than 1000, problems may occur, so
perhaps the wording should be:

> If the calculated year is less than 1000 or greater than 9999, the behavior is
> undefined.

**Note:** This appears to be a duplicate of [DR 217](../c99/issue0217.md), which advises
no consensus / no change.

It was also pointed out that the Proposed Technical Corrigendum does not fix all
of the issues, such as if `tm_mon=4` and `tm_mday=31`, both valid numbers, but
not a valid date.

### Technical Corrigendum

Add after the example code, and before the "Returns" section, the following new
paragraph:

> If any of the fields of the `tm` structure pointed to by `timeptr` contain
> values that are outside the normal ranges\*, the behavior of `asctime()` is
> undefined. If the calculated year exceeds four digits, or is less than the year
> 1000, the behavior is undefined.

Add footnote \*:

> See 7.23.1 para 4 for the specifications of the "normal ranges".
