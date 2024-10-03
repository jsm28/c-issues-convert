### Summary

C11 (and C99 before it) state for both **ungetc()** and **ungetwc()** that

> A successful intervening call (with the stream pointed to by stream) to a file
> positioning function (fseek, fsetpos, or rewind) discards any pushed-back
> characters for the stream. ... The value of the file position indicator for the
> stream after reading or discarding all pushed-back characters shall be the same
> as it was before the characters were pushed back.

(7.21.7.10 p2 \& p5, with similar at 7.29.3.10 p2 \& p5). The "or discarding"
phrasing in p5 makes no sense: all of the listed functions which discard the
push back also \_set\_ the file position. The file position will end up as
whatever the function sets it to, not "the same as it was before the characters
were pushed back".

### Suggested Change

Change

> The value of the file position indicator for the stream after reading or
> discarding all pushed-back characters shall be the same as it was before the
> characters were pushed back.

to

> The value of the file position indicator for the stream after all pushed-back
> characters have been read shall be the same as it was before the characters were
> pushed back.
