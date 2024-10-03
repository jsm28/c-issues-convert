Could you tell me if it is legitimate for a conforming C compiler to perform
what's commonly referred to as dead-store elimination for the first assignment
in the following code fragment:

```c
auto int flag;      /* non-volatile */
 ...
 flag = 1;
 flag = f();
```

If it is valid to do so, then consider

```c
auto int flag;      /* non-volatile */
 if (setjmp(buf))
    {
     if (flag == 1) ...
    }
 flag = 1;
 flag = f();
```

where function `f` invokes `longjmp`. Is the result of the relational expression
defined? A solution might be to define `flag` as `volatile`, but `flag` is *not*
really volatile, and the programmer may not wish to degrade all references to
`flag` nor to locate all such possible `flag`s and lie about their volatility. A
related issue is that in many existing applications, users have coded
`setjmp`-like mechanisms based on a particular operational environment. The
functions do not have the name “`setjmp`,” but essentially establish an
externally accessible entry point within the containing function. Sometimes,
pointers are set to reference such functions, even though the standard precludes
this from being done with `setjmp` itself since it is allowable that it only be
provided as a macro.

There are a number of additional optimizations which must be inhibited across
the actual invocation of `setjmp`, or a `setjmp`-like function. Always avoiding
these optimizations as well as the dead-store elimination shown in the example
may make the program safe for non-local jumps, but unnecessarily penalizes
programs that don't use `setjmp`. To circumvent this problem, some implementors
have defined a pragma which is included in `setjmp.h` to identify “`setjmp`” as
having the property of establishing an externally accessible entry, i.e.,
defining an otherwise non-obvious point of control flow. Other implementations
have hard-coded tests for the name “`setjmp`.”

... would you please respond to the question regarding the legitimacy of the
optimization in the first example?
