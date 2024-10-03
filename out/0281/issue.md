### Summary

In 7.23.1 Components of time, `CLOCKS_PER_SEC` is defined as a macro which
expands to a constant expression with type `clock_t`. `CLOCKS_PER_SEC` need not
be a compile time constant expression, but should be a runtime constant. A value
that is unchanged during program execution.

### Suggested Technical Corrigendum
