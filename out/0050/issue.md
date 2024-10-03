Subclause 6.1.3.4 says that the type of a wide character constant is `wchar_t`,
and subclause 6.1.4 says the type of a wide character string is array of
`wchar_t`.

Subclause 7.1.6 says the typedef name `wchar_t` must be defined in `<stddef.h>`.

Question: When a compiler sees a literal of the form `L'...'` or `L"..."` must
it not check that

1. The name `wchar_t` is visible at that place.
2. The name is a typedef name. It could be redefined in an inner scope.
3. It is a typedef for an integral type. Again, it could be redefined.

And then, take that integral type as the meaning of `wchar_t`. I suppose it
cannot just hope for the best and take a type that makes it feel good.
