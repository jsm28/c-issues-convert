## Issue 0CFP.07: Part 1: Editorial changes

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2016-09-10  
Reference document: [N2077](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2077.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

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

---

Comment from WG14 on 2018-10-18:

Oct 2016 meeting

### Committee Discussion

The committee agrees that this is a defect and accepts the Suggested Technical
Corrigendum

### Proposed Technical Corrigendum

In 14.5, in the new text for C 7.12.13a.5#2, insert “(as if)” before “to
infinite precision”.
