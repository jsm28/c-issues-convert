### Summary

The first sentence of 6.7.5.2p2 seems to suggest that **any** ordinary
identifier both block scope or function prototype scope and no linkage **has** a
variably modified type. This is clearly wrong.

### Suggested Technical Corrigendum

Rewrite the first sentence of 6.7.5.2p2 to read:

> An ordinary identifier (as defined in 6.2.3) that has a variably modified type
> shall have either block scope or function prototype scope, and no linkage.
