## Issue 0284: Does \<math.h\> define `INT_MIN` and `INT_MAX`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: J11, Douglas Walls (US)  
Date: 2003-02-11  
Reference document: [ISO/IEC WG14 N995](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n995.htm)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_284.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_284.htm)

### Summary

\<math.h\> defines macros in terms of INT\_MIN and INT\_MAX. \<math.h\> defines
functions returning the value of INT\_MIN. It is unclear if inclusion of
\<math.h\> defines INT\_MIN and INT\_MAX or also includes \<limits.h\>.

### Details

The description of \<math.h\> in C99 (section 7.12) says that the macros
FP\_ILOGB0 and FP\_ILOGBNAN are defined in \<math.h\> with values, respectively
INT\_MIN or -INT\_MAX and INT\_MAX or INT\_MIN, but never says that INT\_MIN and
INT\_MAX are defined in \<math.h\>.

The synopsis of 7.12.6.5 The ilogb function says:

```c
        #include <math.h>
        int ilogb(double x);
        int ilogbf(float x);
        int ilogbl(long double x);
```

The description of 7.12.6.5 The ilogb functions says "if x is infinite they
compute the value INT\_MAX;".

Does this mean that \<math.h\> includes \<limits.h\>?

Does this mean that \<math.h\> defines INT\_MIN and INT\_MAX?

### Suggested Technical Corrigendum

---

Comment from WG14 on 2004-03-05:

### Committee Response

No Standard library header includes another Standard library header. The header
`<math.h>` does not define `INT_MIN` or `INT_MAX`. A program that wants to check
the return value for equality with one of these macros must include
`<limits.h>`.
