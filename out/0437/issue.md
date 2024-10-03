### Summary

C11 (and C99 before it) state for **clock()** that

> If the processor time used is not available or its value cannot be represented,
> the function returns the value (clock\_t)(-1).

(C11 7.27.2.1 p3). Footnote 319 also states

> In order to measure the time spent in a program, the clock function should be
> called at the start of the program and its return value subtracted from the
> value returned by subsequent calls.

The normative requirement implies that if more processor time has passed than
can be fit into a variable of type **clock\_t** the function must fail and
return **(clock\_t)-1**.

However, existing implementations almost exclusively ignore this requirement and
if more ticks pass than can fit into a **clock\_t** the implementation simply
truncates the value and return the lowermost bits of the actual value. In
programming environments where clock\_t is a 32-bit integer type and
CLOCKS\_PER\_SEC is one million (a very common implementation), clock() will
start misreporting in less than 36 minutes of processor time for signed
clock\_t, or 72 minutes for unsigned clock\_t.

*Question 1:* Are such implementations conforming? If not, should the standard
be altered in any way to permit this *de-facto* standard implementation?

*Question 2:* Should the standard define some limit macros for clock\_t
(effectively defining new values in limits.h for CLOCK\_MAX, the minimum maximum
value for a clock\_t)?

*Question 3:* If the value is truncated and clock\_t is a signed type, the
recommended application usage n footnote 319 (subtracting clock\_t values to
measure intervals) can cause the application to invoke undefined behavior via
integer overflow. In particular, if the initial call to clock() returned A \> 0
(by virtue of some processor time having been consumed before the start of
main() or the point of first measurement), and a subsequent call returned
B\=INT\_MIN just after overflow, then the recommended practice of computing B-A
invokes undefined behavior. Should there be any warning of this included in the
footnote?

### Suggested Change

Given that the vast majority of surveyed implementations appear to have
implemented clock with a simple incrementing counter with no check for overflow,
the requirement for **clock()** to return **(clock\_t)-1** when the number of
clock ticks cannot be represented in a variable of type clock\_t should be
relaxed:

At 7.27.2.1 paragraph 3, change:

> If the processor time used is not available or its value cannot be represented,
> the function returns the value (clock\_t)(-1).

to:

> If the processor time used is not available, the function returns the value
> (clock\_t)-1.

(thus leaving the behavior on overflow unspecified). Change footnote 319 to:

> In order to measure the time spent in a program, the clock function should be
> called at the start of the program and its return value subtracted from the
> value returned by subsequent calls. Note, however, that such a subtraction may
> result in undefined behavior if clock\_t is an unsigned integer type.
