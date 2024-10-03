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
