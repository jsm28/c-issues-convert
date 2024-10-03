### Summary

> `logb(0)` should be considered a pole error in the base standard (it already is
> in Annex F).

### Details

> `logb(0)` is inconsistent between 7.12.6.11 (domain error) and Annex F (range
> error via divide-by-zero).
> 
> `logb(0)` is effectively the same as `log(0)`, `log2(0)`, or `log10(0)`, all of
> which are a pole or singularity error, which is a divide-by-zero exception to
> Annex F and a range error to 7.12. But, `logb` treats it as a domain error in
> 7.12.6.11.

### Suggested Technical Corrigendum

In 7.12.6.11 `logb`:

Change:

> A domain error may occur if the argument is zero.

to

> A range error may occur if the argument is zero.
