## Issue 0331: permit `FE_DIVBYZERO` when `errno` says `EDOM`

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: P. J. Plauger, J11  
Date: 2006-08-01  
Reference document: [N1184](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1184.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_331.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_331.htm)

### Summary

Regarding 7.12.1 para 2,

> which says that if both `errno` and fp exceptions are used, and if a domain
> error occurs, then `errno` gets `EDOM` and the fp exception is `FP_INVALID`:

The purpose of this document is to initiate a formal potential defect report to
request that `FE_DIVBYZERO` can also be acceptable here.  
My previous emails contained a substantive typo which may have created
unnecessary confusions.

### Suggested Technical Corrigendum

---

Comment from WG14 on 2007-10-10:

### Committee Discussion (for history only)

#### Fall 2006

At the fall meeting it was suggested that there need not be a change to 7.12.1.
No consensus was reached, leave in *open* status.

#### Spring 2007

In London the consensus was that no change is required.

### Proposed Committee Response

The Standard seems clear, no change is needed.
