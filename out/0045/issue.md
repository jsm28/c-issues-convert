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
