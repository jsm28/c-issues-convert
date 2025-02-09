### Summary

The sentence describing a preprocessing directive is fearsomely long.

### Suggested Technical Corrigendum

Change 6.10p2:

> A preprocessing directive consists of a sequence of preprocessing tokens
> <del>that begins with</del> <ins>. The first token in the sequence is</ins> a
> `#` preprocessing token that (at the start of translation phase 4\) is either
> the first character in the source file (optionally after white space containing
> no new-line characters) or that follows white space containing at least one
> new-line character<del>, and is ended by the next</del> <ins>. The last token in
> the sequence is the first</ins> new-line character <ins>that follows the first
> token in the sequence</ins>.<sup>140\)</sup> A new-line character ends the
> preprocessing directive even if it occurs within what would otherwise be an
> invocation of a function-like macro.
