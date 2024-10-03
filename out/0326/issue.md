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
