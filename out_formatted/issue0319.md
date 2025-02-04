## Issue 0319: printf("%a", 1.0) and trailing zeros

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Fred Tydeman (USA)  
Date: 2005-04-04  
Reference document: [ISO/IEC WG14 N1094](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1094.txt)  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_319.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_319.htm)

### Summary

Given that **FLT\_RADIX** is 2, what is the output of:

```c
  double x = 1.0;
  printf("%a", x);
```

In particular, are trailing zeros removed or kept?

Some choices that occur to me are:

1. use the smallest precision for an exact representation of this particular value; in effect, remove trailing zeros.
2. use the smallest precision for an exact representation of all values of this type; in effect, keep trailing zeros.
3. use the smallest precision for an exact representation of all values of all floating-point types; in effect, promote to long double and keep trailing zeros.
4. implementation defined.
5. unspecified.
6. something else.

Some implementations that I have seen do 1, others do 2, and one does both 1 and
2 (value and format dependent). I believe choice 1 is the intended behaviour.

Another way to look at this is: should **%a** act like **%e** (keep trailing
zeros) or **%g** (remove trailing zeros) with respect to trailing zeros? Should
this behaviour depend upon the user specifing a precision?

Some parts of **7.19.6.1 The fprintf function** that are relavent are:

Paragraph 6 on the '**\#**' flag has: "For **g** and **G** conversions, trailing
zeros are *not* removed from the result."

Paragraph 8, section **e,E**, has: "... if the precision is zero and the **\#**
flag is not specified, no decimal-point character appears."

Paragraph 8, section **g,G**, has: "Trailing zeros are removed from the
fractional portion of the result unless the **\#** flag is specified; a
decimal-point character appears only if it is followed by a digit."

Paragraph 8, section **a,A**, has: "... if the precision is missing and
**FLT\_RADIX** is a power of 2, then the precision is sufficient for an exact
representation of the value; ..."

Paragraph 8, section **a,A**, has: "... if the precision is missing and
**FLT\_RADIX** is not a power of 2, then the precision is sufficient to
distinguish values of type **double**, except that trailing zeros may be
omitted; ..."

There are corresponding sections for the wide character versions of the
functions in **7.24.2.1 The fwprintf function**.

### Suggested Technical Corrigendum

Change **7.19.6.1 The fprintf function** sections as follows.

Paragraph 6 on the '**\#**' flag, change the above to: "For **a**, **A**, **g**
and **G** conversions, trailing zeros are *not* removed from the result."

Paragraph 8, section **a,A**, change the above to: "... if the precision is
missing and **FLT\_RADIX** is a power of 2, then the precision is the minimum
sufficient for an exact representation of all values of type **double** (removal
of trailing zeros depends upon the **\#** flag); ..."

Paragraph 8, section **a,A**, change the above to: "... if the precision is
missing and **FLT\_RADIX** is not a power of 2, then the precision is the
minimum sufficient to distinguish values of type **double** (removal of trailing
zeros depends upon the **\#** flag); ..."

Also, update the corresponding sections for the wide character versions of the
functions in **7.24.2.1 The fwprintf function**.

Add to the Rationale in section 7.19.6.1: **%a** (without an explicit precision)
acts like **%g** (removes trailing zeros), while **%.\*a** (with an explicit
precision) acts like **%e** (keeps trailing zeros). This was done to allow two
forms of behaviour while using only one conversion specifier.

---

Comment from WG14 on 2006-04-04:

### Committee Response

The Committee does not believe this is a defect, however the Committee may
consider establishing a rule for removing or not removing trailing zeros at some
point in the future.
