## Issue 0332: `gets` is generally unsafe

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Douglas A. Gwyn \<gwyn@arl.army.mil\>, Gwyn (US)  
Date: 2006-10-17  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_332.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_332.htm)

### Summary

The `gets` function's notorious vulnerability to buffer overrun ought to be
addressed.

**Rationale**

The `gets` function draws much criticism due to its vulnerability to buffer
overrun, which is inherent in its legacy interface specification. Its very
presence in the Standard has been taken by many as evidence of WG14's ineptitude
or lack of concern for software reliability, despite arguments to the contrary.
The Committee may be more favorably regarded within the programming community if
it takes reasonable steps to address this issue.

The recent publication of *TR 24731*, which specifies an alternative function
`gets_s` that could be used instead of `gets`, does not satisfy the critics who
claim that the continuing existence of the `gets` specification in the C
standard amounts to an endorsement of its unsafe use in new programs.

**Discussion**

Consider this representative usage of `gets`:

```c
#include <stdio.h>
static char line[BUFSIZ];     /* BUFSIZ is bigger than any normal text line */
extern void process(char *);
int main(void) {
    while (gets(line))
        process(line);        /* may invoke puts(line), etc. */
    return 0;
}
```

This shows how *convenient* the `gets` interface is. The well-known problem with
this interface occurs when the standard input stream contains a text line longer
than the allocated size of the buffer; because `gets` has no way to know that
size, it blindly continues to store data beyond the end of the array, with
potentially devastating impact on program operation. The infamous 1988 Morris
Internet worm was merely the first of many attacks that exploit this behavior to
breach security in network applications.

What might be done to improve the specification for `gets` so that the safety of
this exceptionally convenient interface can be assured? (I do not recommend
removing it altogether!) It seems evident that the only feasible change would be
to impose a limit on the amount of data transferred. Requiring the programmer to
establish the limit through some additional interface would sacrifice the
convenience. The alternative is to impose some constant limit, in which case the
remaining question is what would be a suitable constant. That can be answered by
examining existing uses of `gets` to determine typical buffer sizes. It appears
that two usage patterns predominate: Using the `BUFSIZ` macro which happens to
be conveniently at hand as a consequence of `#include <stdio.h>`, or using some
assumed text-line length such as 80\.

Restricting the amount of data transferred to only 80 characters may be too
severe for many applications, and in any case it would necessitate the
introduction of a new limit macro such as `LINE_MAX` to provide a convenient way
for programmers to declare suitable buffer arrays. Therefore I recommend instead
that the existing usage of `BUFSIZ` be legitimatized, as follows.

### Suggested Technical Corrigendum

Add the following sentence to the **Description** in subclause 7.19.7.7 (The
`gets` function)], between the two existing sentences:

> At most `BUFSIZ-1` characters are copied to the array; excessive characters are
> discarded.

(The portion after the semicolon isn't strictly necessary, but it adds clarity.)

**Impact**

The proposed change to the `gets` specification would have the effect of
preventing buffer overruns in many existing applications. Overly long input
lines would be silently truncated (which is better than the alternative of
treating them as multiple lines).

Existing applications using small buffers would not be automatically rescued by
this change; however, there would be a simple source-code fix (change the buffer
size). New applications would obtain safe behavior by using the known limit for
buffer allocation, exactly as in the above example.

Adoption of such a change would demonstrate the committee's willingness to
improve specifications compatibly with the existing standard, without resorting
to unnecessarily drastic measures.

---

Comment from WG14 on 2007-09-06:

### Committee Discussion (for history only)

The Committee thinks that the programming community would be better served by
flagging the `gets()` function as deprecated.

### Technical Corrigendum

Add to subclause 7.26.9:

> The `gets` function is obsolescent, and is deprecated.

Add forward reference in 7.19.7.7 to 7.26.9
