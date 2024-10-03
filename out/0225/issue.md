### Summary

In `<stdlib.h>`, functions `strtod`, `strtof`, and `strtold` should permit an
implementation to recognize either `inf` or `infinity`, and either `nan` or
`nan(`*n-char-sequence<sub>opt</sub>* `)`, not just one of each.

### Suggested Technical Corrigendum

In 7.20.1.3 replace:

> * one of `INF` or `INFINITY`, ignoring case
> * one of `NAN` or `NAN(`*n-char-sequence<sub>opt</sub>* `)`, ignoring case in the `NAN` part, where:

with:

> * either `INF` not followed by `I`, or `INFINITY`, ignoring case
> * either `NAN` not followed by a left parenthesis, or `NAN(`*n-char-sequence<sub>opt</sub>* `)`, ignoring case in the `NAN` part, where:
