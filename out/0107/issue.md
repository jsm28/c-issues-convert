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
