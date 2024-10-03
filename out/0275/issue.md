### Problem

`FE_ALL_EXCEPT` is defined in 7.6#6 as:

> \[#6] The macro
> 
> ```c
>             FE_ALL_EXCEPT
> ```
> 
> is simply the bitwise OR of all floating-point exception macros defined by the
> implementation.

If no floating-point exception macros are defined, is `FE_ALL_EXCEPT`:

* required to be defined as zero
* required to be undefined
* unspecified whether it is either of the above ?

\[This appears to be the only case of its kind.]

### Suggested Technical Corrigendum

Append to 7.6#6:

> If no such macros are defined, `FE_ALL_EXCEPT` can either be defined as 0 or
> left undefined.
