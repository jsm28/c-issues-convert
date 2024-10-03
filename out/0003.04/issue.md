Subclause 6.8.3: Preprocessor directives within actual macro arguments It is a
guiding principle that a macro function and an actual function should be
invokable in as similar fashion as possible. In the latter case, it is not
uncommon to find code with variations of arguments subject to conditional
compilation. This should also compile correctly if an appropriate macro
definition is made for the function.

While conditional compilations within function arguments is not necessarily a
programming style that I would condone, I feel that it is in the interests of
the C programming community at large for such constructs to be well formed, even
if forbidden, and as such make the following requests:

> I would like the Committee to change subclause 6.8.3 to state that `#if`,
> `#ifdef`, `#ifndef`, `#else`, `#elif`, and `#endif` preprocessing directives are
> allowed within actual macro arguments (not necessarily cleanly nested).
> Conversely, I would like `#define` and `#undef` to be formally forbidden within
> macro invocations, as these can result in effects that are dependent on the
> particular implementation of the macro expansions.
