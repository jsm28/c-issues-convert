Subclause 7.9.5.6 says:

> The `setvbuf` function may be used only after the stream ... has been associated
> with an open file and before any other operation is performed on the stream.

There are two related questions associated with this statement.

1\. What does “performed” mean?

a. Does it include attempts that failed (such as `fread` on output file, etc.)?

b. In particular, does it include a failed attempt to `setvbuf`?

c. What about `fprintf(f, "")`?

2\. What does “other operation” mean?

a. Does it include `setvbuf` itself?

b. Are `ferror` and `feof` operations?

c. What about `clearerr`?

Reasons for asking:

It would seem reasonable to try to get a very large buffer in some applications
by attempting to do a `setvbuf` with, say, 1 MB of buffer space. If that fails,
try again with 0.5 MB, etc. Is this allowed?

My *guess* as to the interpretation is as follows:

1\. An operation is “performed” even if it fails for whatever reason.

2\. All functions defined in subclause 7.9 are to be treated as “operations.”

This is unsatisfactory, as the above approach of attempting to find a good
buffer size would fail.

In the Rationale, it states “The general principle is to provide portable code
with a means of requesting the most appropriate popular buffering style, but not
to *require* an implementation to support these styles.” \[Emphasis added.]

I interpret this as saying that `setvbuf` is an advisory call and need not be
acted on. However, my questions above still stand as there seems to be no way of
negotiating an agreement on good acceptable buffer sizes.

I believe that a clarification is required.
