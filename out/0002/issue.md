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
