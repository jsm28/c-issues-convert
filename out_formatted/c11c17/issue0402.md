## Issue 0402: memory model coherence is not aligned with C\+\+11

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Cross-references: [0406](../c11c17/issue0406.md)  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The memory model described in
[N1569](https://www.open-std.org/jtc1/sc22/wg14/prot/n1569.pdf) matches an older
version of the C\+\+0x memory model, one that allowed executions that were not
intended by the designers. The recommandation is to match the C\+\+11 text by
removing the sentence starting 'Furthermore' in 5.1.2.4p22, and including the
following paragraphs in section 5.1.2.4 (Taken from C\+\+
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf),
1.10p15 through 18):

> If an operation `A` that modifies an atomic object `M` happens before an
> operation `B` that modifies `M` , then `A` shall be earlier than `B` in the
> modification order of `M` .
>
> *NOTE:* The requirement above is known as write-write coherence.
>
> If a value computation `A` of an atomic object `M` happens before a value
> computation `B` of `M` , and `A` takes its value from a side effect `X` on `M`,
> then the value computed by `B` shall either be the value stored by `X` or the
> value stored by a side effect `Y` on `M`, where `Y` follows `X` in the
> modification order of `M`.
>
> *NOTE:* The requirement above is known as read-read coherence.
>
> If a value computation `A` of an atomic object `M` happens before an operation
> `B` on `M`, then `A` shall take its value from a side effect `X` on `M`, where
> `X` precedes `B` in the modification order of `M`.
>
> *NOTE:* The requirement above is known as read-write coherence.
>
> If a side effect `X` on an atomic object `M` happens before a value computation
> `B` of `M`, then the evaluation `B` shall take its value from `X` or from a side
> effect `Y` that follows `X` in the modification order of `M`.
>
> *NOTE:* The requirement above is known as write-read coherence.

### Suggested Technical Corrigendum

See above.

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee Discussion

> * The consensus was that this is an oversight, and should be changed as recommended.

Feb 2012 meeting

### Proposed Technical Corrigendum

> In 5.1.2.4 Paragraph 22 starting at the third sentence, add:
>
> > If an operation `A` that modifies an atomic object `M` happens before an
> > operation `B` that modifies `M` , then `A` shall be earlier than `B` in the
> > modification order of `M` .
> >
> > *NOTE:* The requirement above is known as write-write coherence.
> >
> > If a value computation `A` of an atomic object `M` happens before a value
> > computation `B` of `M` , and `A` takes its value from a side effect `X` on `M`,
> > then the value computed by `B` shall either be the value stored by `X` or the
> > value stored by a side effect `Y` on `M`, where `Y` follows `X` in the
> > modification order of `M`.
> >
> > *NOTE:* The requirement above is known as read-read coherence.
> >
> > If a value computation `A` of an atomic object `M` happens before an operation
> > `B` on `M`, then `A` shall take its value from a side effect `X` on `M`, where
> > `X` precedes `B` in the modification order of `M`.
> >
> > *NOTE:* The requirement above is known as read-write coherence.
> >
> > If a side effect `X` on an atomic object `M` happens before a value computation
> > `B` of `M`, then the evaluation `B` shall take its value from `X` or from a side
> > effect `Y` that follows `X` in the modification order of `M`.
> >
> > *NOTE:* The requirement above is known as write-read coherence.
