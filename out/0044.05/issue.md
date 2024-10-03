Revisiting (b) as the correct interpretation of Question 1, it seems the only
possibility for a definition of the macro `offsetof` constitutes use of an
identifier from the reserved name space to define a builtin which interrogates
the translator's symbol table in a fashion analogous to the `sizeof` operator.
Further, this builtin must appear syntactically as a keyword rather than an
identifier to avoid the constraint violation of subclause 6.4, page 55, line 9,
which invalidates the use of what appears to be a function call within that
which is otherwise required to be a constant expression.

Further, implementing an expansion for `offsetof` as described in the previous
paragraph would violate the implementation constraint outlined in Question 2
above, since the expansion would inject preprocessing tokens requiring
recognition of a keyword outside the scope of a strictly conforming program.

In any case, the implication is that the fragment:

```c
#include <stddef.h>
 static struct x {int field1, field2; } s;
 enum fields {F0, F1, F2 = offsetof(struct x,field2), F3 };
```

is either rendered not strictly conforming or the implementation is rendered a
nonconforming implementation.

Alternatively, if the answer to Question 2 above is no, then the following
questions are raised:

Since translation phases 1 through 4 may introduce into the translation unit
token sequences which are not strictly conforming, what mechanism exists, if
any, to determine whether such sequences originated from the program source?

How is one to interpret the meaning of “strictly conforming program” from clause
4, page 3, lines 38-40, given that subclause 5.1.1.1, page 5, lines 12-15 define
the translation unit to be “a source file together with all the headers and
source files included via the preprocessing directive `#include`, less any
source lines skipped by any of the conditional inclusion preprocessing
directives?”

It seems that any program which makes use of the macro `offsetof` in the context
of a constraint requirement mandating an “integer constant expression” will
require use of unspecified, undefined, or implementation-defined behavior.

As near as I can tell, `offsetof` is the only macro defined by the C Standard
which can alter the behavior of a strictly conforming program as a consequence
of its own definition.
