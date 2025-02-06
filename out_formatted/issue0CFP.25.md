## Issue 0CFP.25: P1 totalorder parameters

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, C Floating Point Group  
Date: 2018-09-05  
Reference document: [N2292](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2292.pdf)  
Submitted against: Floating-point TS 18661 (C11 version, 2014-2016)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

The IEC 60559 totalOrder operation provides a total ordering of the canonical
members of the format, including signaling NaNs. Therefore the binding C
function `totalorder`, specified in TS 18661-1, must be able to accept signaling
NaN inputs. Currently the parameters for `totalorder` have floating type, whose
argument passing may convert a signaling NaN argument into a quiet NaN parameter
value. The following suggested changes use pointers to preserve signaling NaN
inputs.

### Suggested Technical Corrigendum

In F.10.12.1 (TS 18661-1), change:

> ```c
> int totalorder(double x, double y);
> ```

to:

> ```c
> int totalorder(double * x, double * y);
> ```

and similarly for the other prototypes in F.10.12.1 and F.10.12.2.

In F.10.12.1 (TS 18661-1), change:

> **Description**  
>
> \[2\] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair of its arguments `x`, `y`.
> These functions are fully specified in IEC 60559\. These functions are
> independent of the current rounding direction mode and raise no floating-point
> exceptions, even if an argument is a signaling NaN.  
>
> **Returns**  
>
> \[3\] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair of its arguments `x`, `y`.

to:

> **Description**  
>
> \[2\] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair `*x`, `*y`. These functions
> are fully specified in IEC 60559\. These functions are independent of the
> current rounding direction mode and raise no floating-point exceptions, even if
> `*x` or `*y` is a signalling NaN.
>
> **Returns**  
>
> \[3\] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair `*x`, `*y`.

and similarly for F.10.12.2.

---

Comment from WG14 on 2019-05-03:

Oct 2018 meeting

### Committee Discussion

> The committee accepts the Suggested Technical Corrigendum as the Proposed Change
> to resolve this issue.

### Proposed Change

In F.10.12.1 (TS 18661-1), change:

> ```c
> int totalorder(double x, double y);
> ```

to:

> ```c
> int totalorder(double * x, double * y);
> ```

and similarly for the other prototypes in F.10.12.1 and F.10.12.2.

In F.10.12.1 (TS 18661-1), change:

> **Description**  
>
> \[2\] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair of its arguments `x`, `y`.
> These functions are fully specified in IEC 60559\. These functions are
> independent of the current rounding direction mode and raise no floating-point
> exceptions, even if an argument is a signaling NaN.  
>
> **Returns**  
>
> \[3\] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair of its arguments `x`, `y`.

to:

> **Description**  
>
> \[2\] The `totalorder` functions determine whether the total order relationship,
> defined by IEC 60559, is true for the ordered pair `*x`, `*y`. These functions
> are fully specified in IEC 60559\. These functions are independent of the
> current rounding direction mode and raise no floating-point exceptions, even if
> `*x` or `*y` is a signalling NaN.
>
> **Returns**  
>
> \[3\] The `totalorder` functions return nonzero if and only if the total order
> relation is true for the ordered pair `*x`, `*y`.

and similarly for F.10.12.2.
