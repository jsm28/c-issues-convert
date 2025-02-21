## Issue 0EMB.17: \[Embedded C 2004 DR#17\]

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-11-15  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

Problem: TR 18037 has in many places the text fragment 'overflow and rounding',
but has also the text 'rounding and overflow'.

Solution: Defect 2 has established that the required order is first to do
rounding and then to do overflow handling; make the text consistent by replacing
the text fragment 'overflow and rounding' by 'rounding and overflow' throughout
the document.

Change: Make the required change in many places (including the title of 4.1.3
and A.4).
