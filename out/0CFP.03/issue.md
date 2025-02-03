### Summary

ISO/IEC TS 18661-1 subclause 5.3 specifies interfaces that are defined or
declared “only if **\_\_STDC\_WANT\_IEC\_60559\_BFP\_EXT\_\_** is defined as a
macro at the point in the source file where the header for the interface is
first included.” C 7.12#1 says **\<tgmath.h\>** includes **\<math.h\>** and
**\<complex.h\>**.

So for

> ```c
> #include <math.h>
> #define __STDC_WANT_IEC_60559_BFP_EXT__
> #include <tgmath.h>
> float f(float x) { return nextup(x); }
> ```

the **nextup** functions in **\<math.h\>** are not declared and the **nextup**
macro in **\<tgmath.h\>** is defined. Since x has type float, the function
determined by the **nextup** macro in **\<tgmath.h\>** is **nextupf**. But is
this function available to be called? Another example. For

> ```c
> #include <limits.h>
> #define __STDC_WANT_IEC_60559_BFP_EXT__
> #include <math.h>
> ...
> ```

the **fromfp** functions in **\<math.h\>** are declared, but the **WIDTH**
macros in **\<limits.h\>**, which are needed for portable use of the **fromfp**
functions, are not defined. In these examples, interfaces provided by one header
are related to interfaces that are not provided by another header, because of
the placement of the **WANT** macros. This leads to ambiguous cases (as in the
first example above) and incomplete feature sets. Later parts of the TS have
their own WANT macros, which compounds the problem. See also Joseph Myers’s
\<[http://www.open-std.org/jtc1/sc22/wg14/13831](https://www.open-std.org/jtc1/sc22/wg14/13831)\>.

The suggested corrigendum below specifies that the same set of **WANT** macros
must be defined at the points in the code where the relevant headers are first
included. This results in fewer combinations of interfaces and provides one sets
of interfaces that is consistent and complete with respect to a given set of
WANT macros.

### Suggested Technical Corrigendum

Page 5: At the end of 5.3, insert:

> After 7.1.2#4, insert:
>
> > \[4a] Some standard headers define or declare identifiers contingent on whether
> > certain macros whose names begin with **\_STDC\_WANT\_IEC\_60559\_** and end
> > with **\_EXT\_** are defined (by the user) at the point in the code where the
> > header is first included. Within a preprocessing translation unit, the same set
> > of such macros shall be defined for the first inclusion of all such headers.
