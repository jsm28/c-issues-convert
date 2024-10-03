### Summary

For consistency with real floating types, the type `float _Complex` should be
promoted by the default argument promotions to `double _Complex`.

### Suggested Technical Corrigendum

Change 6.5.2.2p6 in part, from:

> and arguments that have type `float` are promoted to `double`.

to:

> and arguments that have a corresponding real type of `float` are promoted,
> without change of type domain, to a type whose corresponding real type is
> `double`.
