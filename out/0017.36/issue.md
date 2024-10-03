Qualifiers on function return type

Refer to subclause 6.6.6.4, page 80, line 24-25: “... whose return type is
`void`.”

The behavior of a type qualifier on a function return is explicitly undefined,
according to subclause 6.5.3, page 64, lines 24-25.

This creates a loophole.

An implementation that supports type qualifiers on function return types is not
required to flag the constraint given on page 80\.
