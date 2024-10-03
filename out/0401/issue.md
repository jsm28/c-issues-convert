### Summary

C\+\+11 forbids "happens before" from being cyclic, but this change has not made
its way into C11. In order to fix this, the following sentence (taken from C\+\+
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf),
1.10p12) should be added to 5.1.2.4p18:

> The implementation shall ensure that no program execution demonstrates a cycle
> in the "happens before" relation.  
> 
> NOTE: This cycle would otherwise be possible only through the use of consume
> operations.

### Suggested Technical Corrigendum

See above.
