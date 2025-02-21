## Issue 0003.04: Should preprocessing directives be permitted within macro invokations?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.8.3: Preprocessor directives within actual macro arguments It is a
guiding principle that a macro function and an actual function should be
invokable in as similar fashion as possible. In the latter case, it is not
uncommon to find code with variations of arguments subject to conditional
compilation. This should also compile correctly if an appropriate macro
definition is made for the function.

While conditional compilations within function arguments is not necessarily a
programming style that I would condone, I feel that it is in the interests of
the C programming community at large for such constructs to be well formed, even
if forbidden, and as such make the following requests:

> I would like the Committee to change subclause 6.8.3 to state that `#if`,
> `#ifdef`, `#ifndef`, `#else`, `#elif`, and `#endif` preprocessing directives are
> allowed within actual macro arguments (not necessarily cleanly nested).
> Conversely, I would like `#define` and `#undef` to be formally forbidden within
> macro invocations, as these can result in effects that are dependent on the
> particular implementation of the macro expansions.

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous response to this item from David F. Prosser. The Committee endorses the
substance of this response, which follows: The equivalent of your proposal was
rejected a couple of years ago. Certain Committee members felt that requiring
all preprocessors to recognize these lines as directives was too much. Those
that felt that these lines must be recognized were finally convinced that it was
enough to allow implementations the right to behave in the more orthogonal
manner. (Maybe they figure that the next version of the standard will have to
require this sort of behavior, as all “reasonable” implementations already will
have it by then.)
