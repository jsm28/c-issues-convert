### Summary

### Summary

In CFP email, Fred Tydeman noted:

> Searching for "infinite precision" in part 1, most of them have "(as if) to"
> before it. Except, `ffma`, `ffmal`, `dfmal` which is missing the "(as if)".

Right. In particular, all the functions that round result to narrower type have
“(as if)”, except for the `fma` family.

### Suggested Technical Corrigendum

In 14.5, in the new text for C 7.12.13a.5#2, insert “(as if)” before “to
infinite precision”.
