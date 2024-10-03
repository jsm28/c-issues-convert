### Problem

6.2.1#7 reads in part:

> Any other identifier has scope that begins just after the completion of its
> declarator.

However, nothing says when a declarator is completed. While it seems obvious to
experienced people that this means the syntactic end of the declarator, the term
"complete" has other meanings when discussing declarations and objects, and
therefore it's a bad term to use.

### Suggested Technical Corrigendum

Change the quoted text to:

> Any other identifier has scope that begins just after the end of the full
> declarator it appears in.
