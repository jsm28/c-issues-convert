### Summary

The sentence describing a preprocessing directive is fearsomely long.

### Suggested Technical Corrigendum

Change 6.10p2:

> A preprocessing directive consists of a sequence of preprocessing tokens ~~that
> begins with~~ <u>. The first token in the sequence is</u> a `#` preprocessing
> token that (at the start of translation phase 4\) is either the first character
> in the source file (optionally after white space containing no new-line
> characters) or that follows white space containing at least one new-line
> character~~, and is ended by the next~~ <u>. The last token in the sequence is
> the first</u> new-line character <u>that follows the first token in the
> sequence</u>.<sup>140\)</sup> A new-line character ends the preprocessing
> directive even if it occurs within what would otherwise be an invocation of a
> function-like macro.
