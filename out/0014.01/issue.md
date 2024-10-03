X/Open Reference Number KRT3.159.1

There are conflicting descriptions of the `setjmp()` interface in ISO 9899:1990.
In subclause 7.6 on page 118, line 8, it is stated that “It is unspecified
whether `setjmp` is a macro or an identifier declared with external linkage.”
Throughout the rest of the standard, however, it is referred to as “the `setjmp`
macro”; in addition, the rationale document states that `setjmp` must be
implemented as a macro. Please clarify whether `setjmp` must be implemented as a
macro, or may be a function as well as a macro, or may just be a function.
