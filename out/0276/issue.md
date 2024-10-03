### Problem

The `perror` function (7.19.10.4) is not listed in 7.19.1 as either a byte
input/output function or a wide character output function. I believe it should
be the former.

### Suggested Technical Corrigendum

In 7.19.1#5, fourth bullet, insert `perror` after `gets`.
