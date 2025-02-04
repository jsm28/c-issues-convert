## Issue 0107: Several `assert` questions

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_107.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_107.html)

ANSI/ISO C Defect report #rfg14:

Subclause 7.2.1.1 (**Synopsis**) says:

> ```c
>  #include <assert.h>
>  void assert(int expression);
> ```

This synopsis raises several related questions.

a) May a strictly conforming program contain code which includes an invocation
of the `assert` macro for an expression whose type is not directly convertible
to type `int`? (See examples below.)

b) Must a conforming implementation issue diagnostics for any and all attempts
to invoke the `assert` macro for an expression having some type which is not
directly convertible to type `int`?

Examples:

```c
 #include <assert.h>

 char *cp;
 void (*fp) ();
 struct S { int member; } obj;

 void example ()
        {
 	assert (cp);	/* conforming code?  diagnostic required? */
 	assert (fp);	/* conforming code?  diagnostic required? */
 	assert (obj);	/* conforming code?  diagnostic required? */
        }
```

c) Must a conforming implementation convert the value yielded by the expression
given in an invocation of the assert macro to type `int` before checking to see
if it compares equal to zero?

Example:

```c
#include <assert.h>

 void example ()
        {
 	assert (0.1);	/* must this casue an abort?  must it NOT? */
        }
```

---

Comment from WG14 on 1997-09-23:

### Response

a) The definition of `assert` depends on the `NDEBUG` macro. The **Synopsis**
provides information on how an implementation may use the parameter. If `NDEBUG`
is defined as a macro, the parameter is not used and hence cannot cause
undefined behavior. If `NDEBUG` is not defined as a macro, the implementation
may rely on the parameter having type `int`. Passing a non-`int` argument in
such a context will render the translation unit not strictly conforming.

b) If `NDEBUG` is defined as a macro, the parameter is not used and no
diagnostic should occur. Otherwise, a violation of this requirement results in
undefined behavior, which does not require a diagnostic.

c) No.
