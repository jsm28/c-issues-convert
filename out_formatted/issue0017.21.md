## Issue 0017.21: Is translation phase 4 defined unambiguously?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Derek M. Jones, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-056  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_017.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_017.html)

Self references in translation phase 4

The following queries arise because of the imprecise way in which phase 4
interacts with itself. While processing a token within phase 4 it is sometime
necessary to get the following tokens from the input, i.e. reading the arguments
to a function-like macro. But when getting these tokens it is not clear how many
phases operate on them:

1. Do the following tokens only get processed by phases 1-3?
2. Do the following tokens get processed by phases 1-4?

When an identifier declared as a function-like macro is encountered, how hard
should an implementation try to locate the opening/closing parentheses?

In:

```c
#define lparen (
 #define f_m(a) a
 f_m lparen "abc" )
```

should the object-like macro be expanded while searching for an opening
parenthesis? Or does the lack of a readily available left parenthesis indicate
that the macro should not be expanded?

Subclause 6.8.3, on page 89, lines 34-35 says “... followed by a `(` as the next
preprocessing token ...” This sentence does not help because in translation
phase 4 all tokens are preprocessing tokens. They don't get converted to “real”
tokens until phase 7\. Thus it cannot be argued that `lparen` is not correct in
this situation, because its result is a preprocessing token.

In:

```c
#define i(x) 3
 #define a i(yz
 #define b )
 a b )   /* goes to 3) or 3 */
```

does `b` get expanded to complete the call `i(yz,` or does the parenthesis to
its right get used?

---

Comment from WG14 on 1997-09-23:

### Response

Concerning the first example:

```c
#define lparen (
 #define f_m(a) a
 f_m lparen "abc" )
```

According to subclause 5.1.1.2 **Translation phases**, page 5, lines 25-39, the
translation phases 1-3 do not cause macros to be expanded. Phase 4 does expand.
To apply subclause 6.8.3 **Macro replacement** page 89, lines 34-35 to the
example: Since `lparen` is not `(` in “`f_m lparen "abc" )`,” this construct is
not recognized as a function-like macro invocation. Therefore the example
expands to

```c
f_m("abc")
```

The same principle applies to the second example:

```c
#define i(x) 3
 #define a i(yz
 #define b )
 a b )       /* expands via the following stages: */

 i(yz b )    /* ) delimits the argument list before b is expanded  */
 i([yz ) ])
 3
```

This is how we interpret subclause 6.8.3, page 89, lines 36-38: The sequence of
preprocessing tokens is terminated by the right-parenthesis preprocessing token.
