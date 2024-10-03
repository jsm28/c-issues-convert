H.J. Lu points out that the SVR4 manual explicitly says that `fwrite(ptr, 0, 1,
stream)` returns 0, not 1\. I don't know what the SVID states.

I think it is more mathematically consistent to return 1 in this case. But in
that case `fread(ptr, 0, 1, stream)` should also return 1, but ANSI explicitly
states that it should return 0\. I don't see any reason why these should be
different, so I think it is best to follow existing practice. I think the ANSI
specification for `fwrite` is a mistake; perhaps it should be fixed in the
revision.
