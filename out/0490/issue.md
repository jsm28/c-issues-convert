### Summary

In trying to determine if exp(infinity) is a range error, I have come across an
unwritten assumption (held by many members of the committee) with respect to:
"if \<violation\> then \<consequence\>". WG14 email messages 13920 to 13937
(with subject of: Meaning of IF-THEN) have a discussion of this.

Message 13925 has in part: That these "if-then" statements were meant to follow
the ordinary-language model, where "if \<violation\> then \<consequence\>"
promises that \<violation\> would necessarily lead to \<consequence\>, but
nothing more. That is similar to the Boolean model. But that has to be combined
with a general rule that when the C standard doesn't mention \<consequence\> as
a visible action in some well-defined circumstance, then it is guaranteed that
it does not occur.

Message 13925 also has: There is a related issue: Just because some defined
behavior is allowed to fail, it was not intended that it could always fail.

Message 13937 has in part: In general, when the C standard doesn't say that
something specific is supposed to happen, it intended that nothing happens.
Explicit permission is given for errno to be set under certain circumstances

### Suggested Technical Corrigendum

Add to 4.0 Conformance after paragraph 1, words along the lines of:

> Unless stated otherwise (**errno** is one such otherwise), when the C standard
> doesn't say that something specific is supposed to happen, it is intended that
> nothing happens. Also, just because some defined behavior is allowed to fail, it
> was not intended that it could always fail.
