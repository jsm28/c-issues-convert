**Summary** Given the following declarations:

```c
  void f(int n, int x[static n]);
   void f(int n, int x[n]) {}
```

An example at the end of 6.7.5.3 (p21) indicates that these declarations are
compatible, but it seems like there should also be something about this in
composite types.

1. If some declarations include "static" and some don't, what is the effect?
2. Does `static` only count if it is on the definition?
3. Does it count if it is on the declaration visible for a given call?
