## Issue 0045: Can one `freopen` an already closed file?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: David J. Hendricksen, WG14  
Date: 1992-12-10  
Reference document: X3J11/92-036  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_045.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_045.html)

Under subclause 7.9.5.4 **The `freopen` function**, the C Standard states on
page 130, lines 24-29:

> The `freopen` function opens the file whose name is the string pointed to by
> `filename` and associates the stream pointed to by `stream` with it. The `mode`
> argument is used just as in the `fopen` function.
>
> The `freopen` function first attempts to close any file that is associated with
> the specified stream. Failure to close the file successfully is ignored. The
> error and end-of-file indicators for the stream are cleared.

It is not clear whether the following situations have defined behavior:

1. Calling `freopen` where `stream` points to uninitialized storage. For example:

   ```c
           { FILE a, *b;
           b = freopen("c.d", "r", &a);
           }
   ```

   (It may not be possible to detect that the information contained within `a` is
   not valid when the close for `freopen` is attempted.)
2. Calling `freopen` where `stream` is associated with a previously closed file. (The storage pointed to by `stream` may have been deallocated.)

---

Comment from WG14 on 1997-09-23:

### Response

The behavior is undefined in both cases; case (2) is clear from subclause 7.9.3
**Files**, page 126, lines 24-27, “A file may be disassociated from a
controlling stream by *closing* the file... The value of a pointer to a `FILE`
object is indeterminate after the associated file is closed (including the
standard text streams).” Also subclause 7.9.3 **Files**, page 126, lines 2-3 and
lines 37-39, “A stream is associated with an external file... by *opening* a
file, ... At program startup, three text streams are predefined and need not be
opened explicitly...” Also subclause 7.9.5.3 **The `fopen` function**, and,
similarly, subclause 7.9.5.4 **The `freopen` function**: “The ... function opens
the file ... and associates a stream with it...” Thus when subclause 7.9.5.4
says “The `freopen` function ... associates the stream pointed to by `stream`
with it,” the intention is certainly that `stream` already points to a valid
stream. Extending this to case (1), we observe that `a` (or `&a`) might not
refer to a stream, since none has been “associated” by any means specified in
the C Standard.
