### Summary

> The description section for `fma()` needs to mention possible overflow and
> underflow errors.

### Details

> All, but one, of the math functions that can overflow have as part of their
> description, a phrase about **range error**. The one function that is missing it
> is `fma()`.
>
> All, but one, of the math functions that can underflow have as part of their
> description, a phrase about **range error**. The one function that is missing it
> is `fma()`.

### Suggested Technical Corrigendum

In 7.12.13.1 `fma` add to description:

> A range error may occur.
