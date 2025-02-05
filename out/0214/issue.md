### Summary

7.20.4.2 reads:

> \[#3\] The implementation shall support the registration of at least 32
> functions.

This does not require registration of a valid function to succeed. The
implementation could fail the first 420 times `atexit()` is called, and then
succeed 32 times. It also does not require `atexit()` to accept any function of
the correct type; theoretically an implementation could reject (say) a function
in a different translation unit.

### Suggested Technical Corrigendum

Change the cited wording to:

> \[#3\] The implementation shall not reject the registration of a valid function
> if less than 32 functions are already registered (multiple registrations of the
> same function counting multiple times).

or add the following words:

> If less than this number are already registered, a call with a valid argument
> shall succeed.
