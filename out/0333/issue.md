### Summary

Defect report [DR\_321](issue:0321) introduced a new pre-defined macro name,
\_\_STDC\_MB\_MIGHT\_NEQ\_WC\_\_ that is conditionally defined by the
implementation. However, this new macro is not in the list of macros that may be
conditionally defined by the implementation in 6.10.8, para 2\.

### Suggested Technical Corrigendum

Add, in proper alphabetic order in the list in 6.10.8 para 2:

> `__STDC_MB_MIGHT_NEQ_WC__` The integer constant `1`, intended to indicate that
> there might be some character *`x`* in the basic character set, such that
> `'`*`x`*`'` need not be equal to `L'`*`x`*`'`.
