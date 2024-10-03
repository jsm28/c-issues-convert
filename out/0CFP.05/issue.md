### Summary

### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14280:

> TS 18661-1 says "Whether C assignment (6.5.16) (and conversion as if by
> assignment) to the same format is an IEC 60559 convertFormat or copy operation
> is implementation-defined, even if `<fenv.h>` defines the macro
> 
> `FE_SNANS_ALWAYS_SIGNAL` (F.2.1).".
> 
> Does this apply to function return, where the return type of the function is the
> same as the type of the expression passed to the return statement and no wider
> evaluation format is in use \- that is, may this act as either convertFormat or
> copy?  C11 F.6 clearly envisages that such a return statement may do a
> conversion to the same type in the case of wider evaluation formats.  But
> 6.8.6.4#3 only refers to conversions "If the expression has a type different
> from the return type of the function in which it appears".

The specification, from F.3#3, quoted above is incomplete in that it doesn’t
cover function returns, which are not assignments or conversions as if by
assignment. As currently written, C11 \+ TS18661-1 might be read to exclude the
possibility of using convertFormat in this case. A statement should be added to
say that the implementation has the option to apply convertFormat to the return
value. The change does not break existing implementations.

The effect of convertFormat would be that signaling NaNs would signal and
noncanonical representations would be canonicalized. It is extremely unlikely
that a program would depend on convertFormat not being used.

### Suggested Technical Corrigendum

In Clause 8, to the text for C F.3#3:

> \[3] Whether C assignment (6.5.16) (and conversion as if by assignment) to the
> same format is an IEC 60559 convertFormat or copy operation is
> implementation-defined, even if `<fenv.h>` defines the macro
> `FE_SNANS_ALWAYS_SIGNAL` (F.2.1).

append the sentence:

> If the return expression of a `return` statement is evaluated to the
> floating-point format of the return type, it is implementation-defined whether a
> convertFormat operation is applied to the result of the return expression.”

At the end of Clause 8, add:

> In F.3#3, attach a footnote to the wording:
> 
> > Whether C assignment (6.5.16) (and conversion as if by assignment) to the same
> > format is an IEC 60559 convertFormat or copy operation
> 
> where the footnote is:
> 
> \*) Where the source and destination formats are the same, convertFormat
> operations differ from copy operations in that convertFormat operations raise
> the “invalid” floating-point exception on signaling NaN inputs and do not
> propagate non-canonical encodings.
