### Summary

C99 7.12.1 Treatment of error conditions paragraph 1 has: Each function shall
execute as if it were a single operation without generating any externally
visible exceptional conditions.

As written, I believe that means that `errno` cannot be altered by any math
function, nor can any of the floating-point exceptions mentioned later in 7.12.1
("invalid", "divide-by-zero", "overflow", "underflow") be raised by any math
function.

That was not our intent.

Seems to me that there are two problems with that text in 7.12.1:

* It should include the word "spurious".
* It should explicitly exclude the "inexact" floating-point exception.

### Suggested Technical Corrigendum
