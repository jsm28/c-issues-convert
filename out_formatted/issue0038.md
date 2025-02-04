## Issue 0038: What happens when macro replacement creates adjacent tokens that can be taken as a single token?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Kuo-Wei Lee, WG14  
Date: 1992-12-10  
Reference document: X3J11/91-046  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_038.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_038.html)

Under subclause 6.8.3.1 **Argument substitution**, the C Standard states on page
90, lines 12-14:

> Before being substituted, each argument's preprocessing tokens are completely
> macro replaced as if they form the rest of the translation unit; no other
> preprocessing tokens are available.

It is not clear to us what should happen if, after the first replacement, the
argument is a valid preprocessing number. Consider the following example:

```c
#define X 0x000E
 #define Y 0x0100
 #define FOO(a) a
 FOO(X+Y)
```

After `X` is replaced, `FOO(X+Y)` becomes `FOO(0x000E+Y)`. At this point, should
the macro replacement continue and expand `Y` to be 0x0100 with the final result
being `FOO(0x000E+0x0100)`; or should the expansion stop since `0x000E+Y` is a
syntactically valid preprocessing number?

In other words, should `FOO(X+Y)` be expanded into `FOO(0x000E+0x0100)`, or
should it be `FOO(0x000E+Y)`?

---

Comment from WG14 on 1997-09-23:

### Response

Subclause 5.1.1.2, page 5, lines 32-39 indicate that translation must proceed as
if all creation of preprocessing tokens completes before any macro expansion
begins. These are translation phases 3 and 4:

> 3\. The source file is decomposed into preprocessing tokens and sequences of
> white-space characters (including comments)...
>
> 4\. Preprocessing directives are executed and macro invocations are expanded.

Therefore, if `X+Y` were expanded to `0x000E+Y`, a new preprocessing number
would not be created. The macro expansion proceeds as follows.

```c
FOO(X+Y) (6 tokens) --
 FOO(0x000E+0x0100) (6 tokens) --
 0x000E+0x0100 (3 tokens)
```

This sequence is required by subclause 6.8.3.1, page 90, lines 10-14:

> A parameter in the replacement list ... is replaced by the corresponding
> argument after all macros contained therein have been expanded. Before being
> substituted, each argument's preprocessing tokens are completely macro replaced
> as if they formed the rest of the translation unit...
