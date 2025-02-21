## Issue 0003.03: Is an empty macro argument a constraint violation?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Terence David Carroll, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-011  
Submitted against: C90  
Status: Closed  
Cross-references: [0153](../c90/issue0153.md)  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_003.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_003.html)

Subclause 6.8.3: Empty arguments to function-like macros I would like to make a
request for clarification and a request for a stronger statement of
standardization. Given

```c
#define macro( xx ) xx
         macro()
```

is this a constraint violation of subclause 6.8.3 **Constraints** paragraph 4:

> The number of arguments in an invocation of a function-like macro shall agree
> with the number of parameters in the macro definition, ...

or is this an undefined, implementation-dependent program \- subclause 6.8.3,
**Semantics** paragraph 5:

> If (before argument substitution) any argument consists of no preprocessing
> tokens, the behavior is undefined.

In connection with the above I would request that the Committee make a much
stronger statement as to whether empty arguments are to be treated as valid
arguments or are to be treated as errors. They can have their uses, but if that
is recognized then it should be standardized; if not, it should not be allowed.

---

Comment from WG14 on 1997-09-23:

### Response

If one takes the general case, empty arguments in invocations of function-like
macros are easy to recognize:

```c
#define f(a,b,c) whatever

         f(,,)
```

These empty arguments all have “shadows” that cause the sentence you reference
in subclause 6.8.3 (page 90, lines 4-5) to be clearly in effect.

The only uncertain case is one in which an empty argument in an invocation of a
one-parameter function-like macro mimics a “no arguments” invocation. (It should
also be noted that the definition of a macro argument from clause 3 does not
preclude an empty sequence.) Thus the standard is clear that the behavior is
undefined in the example from your request. If an implementation does not choose
to allow empty arguments, a diagnostic will probably be emitted; otherwise, the
invocation will most likely be replaced by a preprocessing token sequence in
which the parameter is replaced with no tokens. But because the standard does
not define this, other than as a common extension, there are no guarantees.
