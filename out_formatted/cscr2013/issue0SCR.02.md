## Issue 0SCR.02: Missing formatted input/output functions in Rule 5.40

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Clive Pygott  
Date: 2016-03-01  
Reference document: [N2006](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2006.htm)  
Submitted against: C Secure Coding Rules TS 17961:2013  
Status: Fixed  
Fixed in: C Secure Coding Rules TS 17961:202y  
Converted from: [n2150.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2150.htm)

### Summary

This suggestion comes from MISRA, as they are adding support for 17961 to their
rules.

Rule 5.40 names a number of functions that can attempt to write beyond the
bounds of the target array, if supplied with tainted input, namely: fscanf,
scanf, vfscanf, vscanf, sscanf, vsscanf and sprintf.

The observation is that vsprintf should be included in this list. Also the \_s
versions of all the above (including vsprintf\_s) should be included, as they
also can write beyond the end of the target array.

It is suggested that this is a defect rather than an enhancement, as from the
rationale for the rule, they should have been included when drafted.

---

Comment from WG14 on 2017-04-07:

Apr 2016 meeting

### Committee Discussion

> The committee agrees with the author.

### Proposed Technical Corrigendum

To 5.40 Rule section first sentence change:

> Calls to the `fscanf`, `scanf`, `vfscanf`, and `vsscanf` functions that pass...

to

> Calls to the `fscanf`, `scanf`, `vfscanf`, and `vsscanf` functions, and their
> Annex K counterparts `fscanf_s`, `scanf_s`, `vfscanf_s`, and `vsscanf_s`, that
> pass...

To 5.40 Rule section second sentence change:

> Calls to the `sscanf` and `vsscanf` functions

to

> Calls to the `sscanf`, `vsscanf`, `sscanf_s`, and `vsscanf_s` functions

To 5.40 Rule section third sentence change:

> Calls to the `sprintf` function that

to

> Calls to the `sprintf`, `vsprintf`, `sprintf_s`, and `vsprintf_s` functions that
