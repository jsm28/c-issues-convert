## Issue 0437: `clock` overflow problems

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Austin Group, Nick Stoughton (US)  
Date: 2013-06-19  
Reference document: [N1719](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1719.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

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

---

Comment from WG14 on 2017-11-03:

Oct 2013 meeting

### Committee Discussion

* This issue is tied to Austin Group Defect #686.
* The committee feels that the core issue regards required behavior under the condition that overflow occurs in the implementations choice for the representation of `clock_t`.
* It is noted that many and possibly most implementations have chosen an integer `clock_t` size that overflows early and often.
* The standard does seem to require that the overflow condition is detected and that the corresponding return value shall be that of failure `(clock_t)-1`.
* Such detection runs counter to the desired behavior of the clock counter as being that of highest implementation efficiency, and to subsequent uses across durations that do not exhibit overflow after the first occurrence.
* The suggested technical corrigendum does not appear to discuss or address this core issue and warrants further discussion. The following suggestion for the footnote is offered:
  > Implementations commonly use an integer `clock_t` type that can overflow in as
  > little as 36 minutes. All uses of `clock()` to measure a duration of time must
  > address the issue of possible overflow.

Apr 2014 meeting

### Committee Discussion

> The author will be solicited for a revised technical corrigendum.

Oct 2014 meeting

### Committee Discussion

> There was no paper submitted on this topic, and the committee will again solicit
> the Austin Group for direction.

Apr 2015 meeting

### Committee Discussion

> The paper [N1895](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1895.htm)
> was provided and discussed. The general sentiment in the committee is that
> `clock_t` is underspecified and that this function should be deprecated and
> replaced in a revision to the standard with something that uses, perhaps,
> `struct timespec`. In particular, no implementations are known to implement the
> `-1` return value on overflow.
>
> The committee reviewed the following words and approved them as the Proposed
> Technical Corrigendum.

### Proposed Committee Response

> To question 1, such programs are not conforming and, no, the standard should not
> be altered to accept this behavior.
>
> To question 2, no, this is not the direction.
>
> To question 3, the committee does not agree that this invokes undefined
> behavior. The value returned under such conditions is unspecified.

### Proposed Technical Corrigendum

In 7.27.2.1p3 change:

> If the processor time used is not available or its value cannot be represented,
> the function returns the value `(clock_t)(-1)`<sup>319</sup>. ...
>
> 319\) In order to measure the time spent in a program, the `clock` function
> should be called at the start of the program and its return value subtracted
> from the value returned by subsequent calls.

to

> If the processor time used is not available, the function returns the value
> `(clock_t)(-1)`. If the value cannot be represented, the function returns an
> unspecified value<sup>319</sup>. ...
>
> 319\) This may be due to overflow of the `clock_t` type.
