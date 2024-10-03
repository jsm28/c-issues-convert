When an array of `char` (or `wchar_t`) is initialized with a string literal that
contains fewer characters than the array, are the remaining elements of the
array initialized?

Subclause 6.5.7 **Initialization**, page 72, only says (emphasis mine):

> If there are fewer initializers in a *brace-enclosed list* than there are
> members of an aggregate, the remainder of the aggregate shall be initialized
> implicitly the same as objects that have static storage duration.
