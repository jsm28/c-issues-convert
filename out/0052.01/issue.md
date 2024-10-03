In subclause 7.12.2.3, page 172, the example is not strictly conforming. The
`mktime` return is compared against `-1` instead of `(time_t)-1`, which could
cause a problem with a strictly conforming implementation.
