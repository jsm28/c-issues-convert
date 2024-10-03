Header name tokenization

There is an inconsistency between subclause 6.1.7, page 33, line 8 and the
description of the creation of header name preprocessing tokens.

The “shall” on page 32, line 33 does not limit the creation of header name
preprocessing tokens to within `#include` directives. It simply states that they
would cause a constraint error in this context.

Subclause 6.1.7, page 33, line 8 should read {`0x3`}{`<1/a.h>`}{`1e2`}, or extra
text needs to be added to subclause 6.1.7.

I have not met anybody who expects `if (a<b || c>d)` to parse as {`if`} {`(`}
{`a`} {`<b || c>`} {`d`} {`)`}.
