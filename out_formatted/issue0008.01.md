## Issue 0008.01: Is dead-store elimination permitted near `setjmp`?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Otto R. Newman, WG14  
Date: 1992-12-10  
Reference document: X3J11/90-021  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_008.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_008.html)

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

---

Comment from WG14 on 1997-09-23:

### Response

The relevant citation is subclause 7.6.2.1:

> All accessible objects have values as of the time `longjmp` was called, except
> that the values of objects of automatic storage duration that are local to the
> function containing the invocation of the corresponding `setjmp` macro that do
> not have volatile-qualified type and have been changed between the `setjmp`
> invocation and `longjmp` call are indeterminate.

In response to your question about the effect on optimizations of `setjmp`: Yes,
it is legitimate for a compiler to perform optimizations that eliminate dead
stores to local, non-volatile, automatic variables when `setjmp` is used.
Subclause 7.6.2.1 makes the values of all such variables indeterminate after the
`longjmp` is called. This grants a compiler the liberty to perform dead-store
elimination as well as several other optimizations.
