### Summary

The definition of the `asctime` function involves a `sprintf` call writing into
a buffer of size 26\. This call will have undefined behaviour if the year being
represented falls outside the range \[-999, 9999]. Since applications may have
relied on the size of 26, this should not be corrected by allowing the
implementation to generate a longer string. This is a defect because the
specification is not self-consistent and does not restrict the domain of the
argument.

### Suggested Technical Corrigendum

Append to 7.23.3.1\[#2]:

> except that if the value of `timeptr->tm_year` is outside the range \[-2899,
> 8099] (and thus the represented year will not fit into four characters) it is
> replaced by up to 4 implementation-defined characters.
