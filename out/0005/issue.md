According to subclause 6.8.6, a pragma directive “causes the implementation to
behave in an implementation-defined manner.” May a conforming implementation
define and recognize a pragma which would change the semantics of the language?
For example, might a conforming implementation recognize and honor the directive

```c
#pragma UNSIGNED_PRESERVING
```

as a way for a program to request non-standard integral promotions?

I also pose the corollary question. May a strictly conforming program contain a
pragma directive? According to subclause 4, a strictly conforming program “shall
use only those features of the language ... specified in this standard. It shall
not produce output dependent on any unspecified, undefined, or
implementation-defined behavior...”

If there is no constraint on how a conforming implementation may behave when
encountering a pragma directive, would it not follow that a strictly conforming
program may not contain a pragma directive?
