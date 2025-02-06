## Issue 0CFP.18: P4: missing specification of preferred quantum exponents

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, C Floating Point Group  
Date: 2018-02-22  
Reference document: [N2204](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2204.pdf)  
Submitted against: Floating-point TS 18661 (C11 version, 2014-2016)  
Status: Fixed  
Fixed in: C23, Floating-point TS 18661-4:2025  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

TS 18661-4 neglected to specify the preferred quantum exponent for its new
functions. This was an oversight. The following suggested TC adds the missing
specification.

### Suggested Technical Corrigendum

In TS 18661-4, at the end of clause 7, append:

In the Preferred Quantum Exponents table in 5.2.4.2.2a#7, insert before the
final row:

|  |  |
| --- | --- |
| ```c rsqrt ``` | −floor(Q(`x`)/2) |
| ```c compoundn ``` | floor(`n` × min(0, Q(`x`))) |
| ```c rootn ``` | floor(Q(`x`)/`n`) |
| ```c pown ``` | floor(`n` × Q(`x`)) |
| ```c powr ``` | floor(`y` × Q(`x`)) |

In TS 18661-4, at the end of clause 8, append:

In the Preferred Exponents Table in 5.2.4.2.2a#7, append:

|  |  |
| --- | --- |
| reduction functions | unspecified |

---

Comment from WG14 on 2018-10-18:

Apr 2018 meeting

### Committee Discussion

> The committee accepted the Suggested Technical Corrigendum as the Proposed
> Change (using our new terminology).

### Proposed Change

In TS 18661-4, at the end of clause 7, append:

In the Preferred Quantum Exponents table in 5.2.4.2.2a#7, insert before the
final row:

|  |  |
| --- | --- |
| ```c rsqrt ``` | −floor(Q(`x`)/2) |
| ```c compoundn ``` | floor(`n` × min(0, Q(`x`))) |
| ```c rootn ``` | floor(Q(`x`)/`n`) |
| ```c pown ``` | floor(`n` × Q(`x`)) |
| ```c powr ``` | floor(`y` × Q(`x`)) |

In TS 18661-4, at the end of clause 8, append:

In the Preferred Exponents Table in 5.2.4.2.2a#7, append:

|  |  |
| --- | --- |
| reduction functions | unspecified |
