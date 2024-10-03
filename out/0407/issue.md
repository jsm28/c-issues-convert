### Summary

C11 seems to omit the restriction imposed in C\+\+11 in 29.3p7 (from
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf)):

> For atomic operations `A` and `B` on an atomic object `M`, if there are
> `memory_order_seq_cst fences X` and `Y` such that `A`is sequenced before `X`,
> `Y` is sequenced before `B`, and `X` precedes `Y` in `S`, then `B` occurs later
> than `A` in the modification order of `M`.

Furthermore, it seems that both C11 and C\+\+11 are missing the following two
derivatives of this rule:

> For atomic modifications `A` and `B` of an atomic object `M`, if there is a
> `memory_order_seq_cst fence X` such that `A` is sequenced before `X`, and `X`
> precedes `B` in `S`, then `B` occurs later than `A` in the modification order of
> `M`.
> 
> For atomic modifications `A` and `B` of an atomic object `M`, if there is a
> `memory_order_seq_cst` fence `Y` such that `Y` is sequenced before `B`, and `A`
> precedes `Y` in `S`, then `B` occurs later than `A` in the modification order of
> `M`.

### Suggested Technical Corrigendum

See above.
