## Issue 0002: Should `\` be escaped within macro actual parameters?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-010  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_002.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_002.html)

Subclause 6.8.3.2: Semantics of `#`

A minor detail in the semantics is that it does not explicitly state that a `\`
character will be inserted before a `\` character that occurs within a macro
actual parameter, only when the `\` character occurs within a string literal or
character constant within the actual parameter.

I can see that there is an argument concerning the systems where `\` is a valid
part of a path name and where `#include` path names are desired to be built
dynamically and then `#`ed.

Would it not be better, however, to escape all `\` within actual parameters and
require either

a. that systems using `\` in path names escape them within`#include` strings, or
perhaps

b. that during macro processing of `#include` parameters the `#` operator will
not cause `\` characters to be escaped at all or will be implementation defined?

This second case (b) is better, as strings for `#include` directives are already
a special case (no escape processing, etc.), so should not the `#` operator also
be special for `#include` directives?

---

Comment from WG14 on 1997-09-23:

### Response

The Committee reasserts that the grammar and/or semantics of preprocessing as
they appear in the standard are as intended. We are attaching a copy of the
previous response to this item from David F. Prosser (Editor of the standard).
The Committee endorses the substance of this response, which follows: The rules
in subclause 6.8.3.2 regarding `\` were discussed in the Committee and the
result is as intended. The Committee's charter was to standardize prior art
where such was clear, and the behavior of those C preprocessing phases that
allowed tokens such as `\` left them alone, even when inserting them into
strings. However, the Committee also had license to fix or add to the language
where it was judged to be deficient. Since none of the existing stringizing
preprocessing phases correctly handled string literals and certain character
constants, the special rules for these were chosen. Subclause 6.8.3's examples
(page 92, lines 4-33) include a `\` that is outside of a string literal or
character constant. If the rules were to be modified along the lines of your
proposal, the intended effect would not happen. One of the main points in your
argument is that uncontained `\`s are only critical in path names that use `\`
as a special character, and that this is only needed when `#include` filenames
are constructed via macro replacement. I agree that the current rules do allow
this sort of use without too much trouble, but I don't see this as being a main
motivation for this feature. By default, the rules for stringizing were that the
original spelling of the invocation argument is placed into a string literal.
The only exceptions made to this were those that were valid C tokens that could
not be simply inserted between a pair of `"`s. The rules for `\` and `"` within
string literals and character constants were derived from that need only.
Furthermore, a lone `\` is a preprocessing token due to the “some other
character” rule of the syntax from subclause 6.1. This would be the only place
where special constraints were placed on one of this type of preprocessing
token.

Finally, solution b) of your discussion involves context-dependent rules for the
stringizing operation. While there is a minor context dependency regarding macro
replacement and the `defined` unary operator on `#if` and `#elif` directive
lines, this is the only context dependency in the whole set of macro replacement
rules. Moreover, this dependency is at the topmost level only. Solution b) would
require a flag noting whether the result of the replacement was to be used
within a `#include` directive. Therefore, the same macro invocation would
produce different results at different invocations. (At the least, debugging
and/or testing of a tricky macroized `#include` directive would be more
difficult.)

In conclusion, to the best of my knowledge, the Committee wants to keep the
behavior here as currently described, and made this choice intentionally.
