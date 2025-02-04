## Issue 0471: Complex math functions cacosh and ctanh

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred Tydeman  
Date: 2014-10-28  
Reference document: [N1886](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1886.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Complex math functions (cacosh (G.6.2.1) and ctanh(G.6.2.6)) are incorrectly
specified.

1. cacosh( 0.0 \+ I\*NaN ) should be NaN \+ I\*pi/2 (not NaN \+ I\*NaN).

Reasons: Mathematically, cacosh(0.0\+I\*y) \= asinh(y) \+ I\*pi/2. Also, C
requires cacos(0\+I\*NaN) to be pi/2\+I\*NAN, which along with the
mathematically identity cacosh(z) \= \+/-I \* cacos(z), means cacosh(0.0 \+
I\*NaN) is NaN \+ I\*pi/2.

3. ctanh(\+0.0\+I\*NaN) should be 0.0 \+ I\*NaN (not NaN\+I\*NaN)
4. ctanh(\+0.0\+I\*INF) should be 0.0 \+ I\*NaN w/ invalid (not NaN\+I\*NaN w/ invalid)

Reason for above two: Since ctanh(x\+I\*y) \= (sinh(2x) \+ I\*sin(2y)) /
(cosh(2x) \+ cos(2y)), for any rational number y, cos(2y) cannot be exactly -1,
so no 0/(1\+(-1)),so no 0/0, so no NaN for the real component of the result


### Suggested Technical Corrigendum

Add to G.6.2.1 cacosh before 4th bullet: cacosh(0.0\+I\*NaN) returns NaN \+
I\*pi/2

Add to G.6.2.1 cacosh 4th bullet: "non-zero" so it reads: cacosh(x \+ iNaN)
returns NaN \+ i\*NaN and optionally raises the “invalid” floating-point
exception, for finite non-zero x.

Add to G.6.2.6 ctanh before 3rd bullet: ctanh(0.0\+I\*INF) returns 0.0\+I\*NAN
and raises the “invalid” floating-point exception.

Add to G.6.2.6 ctanh 3rd bullet: "non-zero" so it reads: ctanh(x \+ I\*INF)
returns NaN \+ i\*NaN and raises the “invalid” floating-point exception, for
finite non-zero x.

Add to G.6.2.6 ctanh before 4th bullet: ctanh(0.0\+I\*NaN) returns 0.0\+I\*NAN

Add to G.6.2.6 ctanh 4th bullet: "non-zero" so it reads: ctanh(x \+ I\*NAN)
returns NaN \+ i\*NaN and optionally raises the “invalid” floating-point
exception, for finite non-zero x.

---

Comment from WG14 on 2017-11-03:

Oct 2014 meeting

### Committee Discussion

> This DR is derived from
> [N1867.](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1867.htm) The
> committee agrees with the Suggested Technical Corrigendum.

Oct 2017 meeting

### Committee Discussion

> In light of the paper
> [N2173](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2173.htm) the
> committee agrees to amend the PTC to specify that
>
> > cacosh(0.0\+*i*NaN) returns NaN ± *i*π/2

### Proposed Technical Corrigendum

Add new paragraph to G.6.2.1 cacosh before 4th bullet:

> cacosh(0.0\+*i*NaN) returns NaN ± *i*π/2

Change G.6.2.1 cacosh 4th bullet from:

> cacosh(x \+ *i*NaN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite x.

to

> cacosh(x \+ *i*NaN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite non-zero x.

Add new paragraph to G.6.2.6 ctanh before 3rd bullet:

> ctanh(0.0\+*i*∞) returns 0.0\+*i*NAN and raises the “invalid” floating-point
> exception.

Change G.6.2.6 ctanh 3rd bullet clause from:

> ctanh(x \+ *i*∞) returns NaN \+ *i*NaN and raises the “invalid” floating-point
> exception, for finite x.

to

> ctanh(x \+ *i*∞) returns NaN \+ *i*NaN and raises the “invalid” floating-point
> exception, for finite non-zero x.

Add new paragraph to G.6.2.6 ctanh before 4th bullet:

> ctanh(0.0\+*i*NaN) returns 0.0\+*i*NAN

Change G.6.2.6 ctanh 4th bullet from:

> ctanh(x \+ *i*NAN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite x.

to

> ctanh(x \+ *i*NAN) returns NaN \+ *i*NaN and optionally raises the “invalid”
> floating-point exception, for finite non-zero x.
