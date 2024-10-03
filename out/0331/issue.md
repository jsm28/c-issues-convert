### Summary

Regarding 7.12.1 para 2,

> which says that if both `errno` and fp exceptions are used, and if a domain
> error occurs, then `errno` gets `EDOM` and the fp exception is `FP_INVALID`:

The purpose of this document is to initiate a formal potential defect report to
request that `FE_DIVBYZERO` can also be acceptable here.  
My previous emails contained a substantive typo which may have created
unnecessary confusions.

### Suggested Technical Corrigendum
