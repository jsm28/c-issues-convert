### Problem

Consider the calls:

```c
   iswctype (c, wctype (property))
    towctrans (c, wctrans (property))
```

where property is not valid in the current locale. The `wctype` and `wctrans`
functions return zero, but the behaviour of `iswctype` and `towctrans` is not
specified.

I believe it would be useful \- and considered natural \- for them to return 0
("`c` does not have this property") and `c` ("`c` is unaffected by this
mapping") respectively.

### Suggested Technical Corrigendum

Append to 7.25.2.2.1#4:

> If `desc` is zero, the `iswctype` function returns zero (false).

Append to 7.25.3.2.1#4:

> If `desc` is zero, the `towctrans` function returns the value of `wc`.
