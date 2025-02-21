## Issue 0490: Unwritten Assumptions About if-then

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2016-01-18  
Reference document: [N1995](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1995.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

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

---

Comment from WG14 on 2017-04-07:

Apr 2016 meeting

### Committee Discussion

> After discussion, the committee consensus was that this was not in fact a
> defect.

### Proposed Committee Response

> This is not a defect.
>
> The Standard is written in English using normal conventions.
