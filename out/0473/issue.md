### Summary

"A range error occurs if **x** is too large." is misleading (or ambiguous) for
expm1 (7.12.6.3p2), erfc (7.12.8.2p2), and lgamma (7.12.8.3p2).

"too large" could mean either \+/-large value (in which case "too small" means
\+/-near zero) or just \+large value (in which case "too small" means -large
value).

7.12.6.3p2: expm1(-DBL\_MAX) is -1, which is not a range error.

7.12.8.2p2: erfc(-DBL\_MAX) is 2, which is not a range error.

7.12.8.3p2: lgamma(-DBL\_MAX) is a pole error, which is not a range error.

### Suggested Technical Corrigendum

Add the word "positive" before **x** in those three cases so that they are:

> A range error occurs if positive **x** is too large.
