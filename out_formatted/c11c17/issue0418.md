## Issue 0418: `fmod(0.,Nan)` and `fmod(Nan, infinity)`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman (USA)  
Date: 2012-09-13  
Reference document: [N1633](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1633.htm)   
 **Related:** [N1497](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1497.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

First question. When Annex F is in effect, what should the value of fmod(0.,NaN)
be? The two choices are 0\. or NaN.

Annex F.10.7.1 The fmod functions has:

> * fmod(\+/-0, y) returns \+/-0 for y not zero.
> * fmod(x, y) returns a NaN and raises the “invalid” floating-point exception for x infinite or y zero (and neither is a NaN).

So, that first bullet item says fmod(0.,NaN) is 0\.

Elsewhere in that annex (F.10 Mathematics, paragraph 11), we have:

> Functions with a NaN argument return a NaN result and raise no floating-point
> exception, except where stated otherwise.

That says that fmod(0.,NaN) is NaN.

One idea is to explicitly add words about a NaN to the first bullet item in
F.10.7.1, such as:

> * fmod(\+/-0, y) returns \+/-0 for y not zero nor NaN.

However, if F.10#11 covers NaN arguments before any other arguments are
considered, then words about NaN could be removed from the second case in
F.10.7.1, such as:

> * fmod(x, y) returns a NaN and raises the “invalid” floating-point exception for x infinite or y zero.

I believe that takes us back to before N1497 was done.

Second question: what should fmod(NaN,infinity) be? Must it be the same NaN
argument, or may it be any NaN?

Annex F.10.7.1 The fmod functions has:

> * fmod(x, \+/-infinity) returns x for x not infinite.

Which says fmod(NaN,infinity) must be the same NaN argument.

But, if F.10#11 covers this NaN argument, then this case is just some NaN.

It appears that the third bullet should either be left alone or changed to:

> * fmod(x, \+/-infinity) returns x for finite x.

Some other functions that discuss NaN arguments in Annex F are: frexp, ilogb,
modf, hypot, pow, fmax, fmin, and fma. Of those, only hypot, pow, fmax, and fmin
have exceptions on NaN in implies NaN out.

---

Comment from WG14 on 2013-04-26:

Oct 2012 meeting

### Committee Discussion

> * Given that, unless stated otherwise, if the argument is a NaN, the result is a NaN, and there is no floating point exception.
> * The parenthetical comment **might** be causing confusion, and removing it seems to make it more confusing.
> * Adding more explicit wording is possible but seems unnecessary.

### Proposed Committee Response

The consensus was to do nothing and the author agrees.
