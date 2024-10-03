### Summary

According to 6.10.1p3, "each preprocessing token \[in a #if directive] is
converted into a token." But what if, for example, the line contains an
unmatched quote mark, or a preprocessing number like 4hello? How is such a
preprocessing token converted into a token? No indication is given that the
conversion may fail.

### Suggested Technical Corrigendum

Insert new constraint paragraph after 6.10.1p1:

> Each preprocessing token that remains after all macro replacements have occurred
> shall be in the lexical form of a token (6.4).
