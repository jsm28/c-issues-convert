### Summary

It has been mathematically proved that a simplification can be made to the
memory model as it is specified in the final draft of the C\+\+11 standard.
Essentially, the restriction defining *visible sequence of side effects* (vsse)
is redundant and can be removed with no ill effects. The main motivation for
doing this is that the current restriction is misleading. 5.1.2.4p22 defines
vsse's:

> The visible sequence of side effects on an atomic object `M`, with respect to a
> value computation `B` of `M`, is a maximal contiguous sub-sequence of side
> effects in the modification order of `M`, where the first side effect is visible
> with respect to `B`, and for every subsequent side effect, it is not the case
> that `B` happens before it. The value of an atomic object `M`, as determined by
> evaluation B, shall be the value stored by some operation in the visible
> sequence of `M` with respect to `B`.

The wording of this paragraph makes it seem as if the vsse identifies the writes
that an atomic read is allowed to read from, but this is not the case. There can
be writes in the vsse that cannot be read due to the coherence requirements (to
be included in C, 1.10p15 through 1.10p18 in C\+\+
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf)).
Consequently this is even more confusing than it at first appears.

Also propose changing 5.1.2.4p22 to the following:

> The value of an atomic object `M`, as determined by evaluation `B`, shall be the
> value stored by some side effect `A` that modifies `M`, where `B` does not
> happen before `A`.

With a note to remind the reader of the coherence requirements:

> *NOTE:* The set of side effects that a given evaluation might take its value
> from is also restricted by the rest of the rules described here, and in
> particular, by the coherence requirements below

If the committee is concerned about allowing a differing text from C\+\+11, then
a note could be added to assure the reader:

> *NOTE:* Although the rules for multi-threaded executions differ here from those
> of C\+\+11, the executions they allow are precisely the same. Visible sequences
> of side effects are a redundant restriction.

### Suggested Technical Corrigendum

See above.
