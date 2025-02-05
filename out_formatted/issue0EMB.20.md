## Issue 0EMB.20: \[Embedded C 2004 DR#20\]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2005-03-03  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1096.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1096.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: the text on the countls function in 4.1.7.3 and 7.18a.6.4 reads:

> The integer return value of the above functions is defined as follows:
>
> * if the value of the fixed-point argument f is non-zero, the return value is the largest integer k for which the expression f\<\<k does not overflow;
> * if the value of the fixed-point argument is zero, an integer value is returned that is at least as large as N-1, where N is the total number of (nonpadding) bits of the fixed-point type of the argument.
>
> Note: if the value of the fixed-point argument is zero, the recommended return
> value is exactly N-1.

In the 'argument is zero' case, for a signed fixed-point type, the notion
'nonpadding bits' includes the sign bit (see 6.2.6.3); this implies that the N
for signed types is one larger that the N for the corresponding unsigned types;
this is wrong (it suggests that shifting into the sign bit does not generate an
overflow). In stead of '(nonpadding) bits', the notion 'value bits' should be
used.

Solution: in 4.1.7.3 and 7.18a.6.4, replace in the 2nd bullet '(nonpadding)' by
'value'.
