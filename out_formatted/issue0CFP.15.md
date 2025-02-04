## Issue 0CFP.15: P3: Characteristic macros for non-arithmetic formats

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Jim Thomas  
Date: 2017-10-25  
Reference document: [N2171](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2171.pdf)  
Submitted against: Floating-point TS 18661 (C11 version)  
Status: Fixed  
Fixed in: C23  
Converted from: [n2397.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2397.htm)

### Summary

This DR addresses an issue related to DR 501 and IEC 60559 non-arithmetic
interchange formats.

TS 18661-3 attempted to change the definition of `DECIMAL_DIG` so that it would
apply to all supported IEC 60559 formats. DR 501 shows that this change is
problematic. After several unsuccessful attempts at a suitable TC, WG 14 and the
CFP group have agreed to obsolesce `DECIMAL_DIG` in favor of the
*type*`_DECIMAL_DIG` macros.

The *type*`_DECIMAL_DIG` macros are helpful in using conversions between binary
floating-point formats and decimal character sequences. TS 18661-3 specifies
such conversions for non-arithmetic binary interchange formats, but neglects to
include the macros for such formats.

Likewise, the *type*`_DIG` macros too are helpful in using conversions between
binary floating-point formats and decimal character sequences, though TS 18661-3
does not specify them for non-arithmetic formats.

The suggested TC below extends the set of `FLT`*N*`_DECIMAL_DIG` and
`FLT`*N*`_DIG` macros to include ones for IEC 60559 non-arithmetic binary
interchange formats.

### Suggested Technical Corrigendum

In TS 18661-3 5.3, in the text for 5.2.4.2.2#6c, after the list for supported
types `_Float`*`N`*, insert:

> for IEC 60559 non-arithmetic binary interchange formats of width *N*:
>
> `FLT`*N*`_DECIMAL_DIG     FLT`*N*`_DIG`

In TS 18661-3 clause 7, in the text for 5.2.4.2.2a#1, change:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type of width
> *N*.

to:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type or a
> non-arithmetic binary interchange format of width *N*.

Change the last sentence of  5.2.4.2.2a#1 from:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following lists.

to:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following list,
> except, the implementation shall define the macros `FLT`*N*`_DECIMAL_DIG` and
> `FLT`*N*`_DIG` if it supports IEC 60559 non-arithmetic binary interchange
> formats of width *N* by providing the encoding-to-encoding conversion functions
> in `<math.h>` and the string-to-encoding and string-from-encoding functions in
> `<stdlib.h>`.

---

Comment from WG14 on 2018-10-18:

Oct 2017 meeting

### Committee Discussion

The committee agreed with this issue and its proposed clarification.

**Proposed Technical Clarification**

In TS 18661-3 5.3, in the text for 5.2.4.2.2#6c, after the list for supported
types `_Float`*`N`*, insert:

> for IEC 60559 non-arithmetic binary interchange formats of width *N*:
>
> `FLT`*N*`_DECIMAL_DIG     FLT`*N*`_DIG`

In TS 18661-3 clause 7, in the text for 5.2.4.2.2a#1, change:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type of width
> *N*.

to:

> The prefix `FLT`*N*`_` indicates a binary interchange floating type or a
> non-arithmetic binary interchange format of width *N*.

Change the last sentence of  5.2.4.2.2a#1 from:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following lists.

to:

> Conversely, for each such type that the implementation does not provide,
> `<float.h>` shall not define the associated macros in the following list,
> except, the implementation shall define the macros `FLT`*N*`_DECIMAL_DIG` and
> `FLT`*N*`_DIG` if it supports IEC 60559 non-arithmetic binary interchange
> formats of width *N* by providing the encoding-to-encoding conversion functions
> in `<math.h>` and the string-to-encoding and string-from-encoding functions in
> `<stdlib.h>`.
