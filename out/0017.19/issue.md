Order of evaluation of macros

Refer to subclause 6.8.3, page 89\. In:

```c
#define f(a) a*g
 #define g(a) f(a)
 f(2)(9)
```

it should be defined whether this results in:

1. ```c
   2*f(9)
   ```
   
   or
2. `2*9*g`

X3J11 previously said, “The behavior in this case could have been specified, but
the Committee has decided more than once not to do so. \[They] do not wish to
promote this sort of macro replacement usage.”

I interpret this as saying, in other words, “If we don't define the behavior
nobody will use it.” Does anybody think this position is unusual?

People seem to agree that the behavior is ambiguous in this case. Should we
specify this case as undefined behavior?
