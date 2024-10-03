`const void` type as a parameter

Refer to subclause 6.5.4.3, page 67, line 37\. `f(const void)` should be
explicitly undefined; also `f(register void)`, `f(volatile void)`, and
combinations thereof.
