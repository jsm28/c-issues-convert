### Summary

Variably modified types are defined by 6.7.5#3:

> \[#3] A *full declarator* is a declarator that is not part of another
> declarator. The end of a full declarator is a sequence point. If the nested
> sequence of declarators in a full declarator contains a variable length array
> type, the type specified by the full declarator is said to be *variably
> modified*.

It is desirable for the definition to look at the declarator rather than just
the resulting type, so that function parameters adjusted from array to pointer
type are variably modified if the array size is variable: in

```c
    void
    f (int i, int a[static ++i])
    {
      // ...
    }
```

the increment of `i` must be evaluated for the definition of `static` in this
context to make sense. However, what it means for the declarators to "contain" a
type is unclear. The natural interpretation is that they include an array
declarator with array size `[*]` or an expression which is not an integer
constant expression. However, this does not cover cases such as

```c
    int x;
    // ...
    typedef int vla[x];
    vla y[3];
```

where a typedef for a variably modified type is used. `y` is a VLA, and clearly
ought to be variably modified, but nothing about the declarators makes it
variably modified; only the declaration specifier does so.

### Suggested Technical Corrigendum
