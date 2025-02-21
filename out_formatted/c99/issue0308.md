## Issue 0308: Clarify that source files et al. need not be "files"

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_308.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_308.htm)

### Summary

I do not recall the specific motivation for adding this note, but it's certainly
true, and it seems harmless.

It should be noted that in the C\+\+ standard, this text is an embedded
non-normative note at the end of the description of phase 7 (parsing and
semantic analysis). But the C standard does not have embedded notes, and the
note is not actually specific to phase 7 (which talks principally about tokens,
without even mentioning files). Adding the text to this footnote, which already
points out an implication of the as-if rule for the phases of translation, would
seem to be the ideal solution.

### Suggested Technical Corrigendum

Change footnote 5 (5.1.1.2p1):

> Implementations shall behave as if these separate phases occur, even though many
> are typically folded together in practice. <ins>Source files, translation units
> and translated translation units need not necessarily be stored as files, nor
> need there be any one-to-one correspondence between these entities and any
> external representation. The description is conceptual only, and does not
> specify any particular implementation.</ins>

---

Comment from WG14 on 2006-03-05:

### Technical Corrigendum

Change footnote 5 (5.1.1.2p1):

> Implementations shall behave as if these separate phases occur, even though many
> are typically folded together in practice. <ins>Source files, translation units
> and translated translation units need not necessarily be stored as files, nor
> need there be any one-to-one correspondence between these entities and any
> external representation. The description is conceptual only, and does not
> specify any particular implementation.</ins>
