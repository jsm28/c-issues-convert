### Summary

The `ctime_s` function in Annex K was defined analogously to `ctime`, and some
of the text from the definition of `ctime` was copied and modified slightly.

K.3.8.2.2p4 states that `ctime_s` is equivalent to the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

In this case, the text from the original `ctime` definition was not quite
modified enough.  The `localtime_s` function takes two arguments and the above
code only supplies one.

### Suggested Technical Corrigendum

In K.3.8.2.2p4, replace

> ```c
> asctime_s(s, maxsize, localtime_s(timer))
> ```

with the following.

> ```c
> asctime_s(s, maxsize, localtime_s(timer, &(struct tm){ 0 }))
> ```
