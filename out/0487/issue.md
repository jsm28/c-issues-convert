### Summary

The standard appears to be inconsistent on `timespec` structure versus `tm`
structure with respect to normative requirements. Both have: The semantics of
the members and their normal ranges are expressed in the comments. But, for
`timespec`, it appears as a footnote, while for `tm`, it appears in the body of
the standard.

### Suggested Technical Corrigendum

Move that sentence from footnote 317 in 7.27.1#4 to be in paragraph 4
