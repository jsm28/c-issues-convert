Are multiple definitions of unused identifiers with external linkage permitted?

The wording in subclause 6.7 permits multiple definitions of identifiers with
external linkage, so long as the identifiers are never used. For example, the
following program is “strictly conforming” if you read the wording in subclause
6.7 literally:

```c
int F() {return 0;}
 int F() {return 1;}
 int V = 0;
 int V = 1;
 int main() {return 0;}
```

This must be a bug in the wording of subclause 6.7. It cannot have been the
Committee's intent, since it prohibits the most commonly encountered linker
model. For example, most linkers will flatly refuse to link the following
“strictly conforming” program

```c
x.c:
```

> ```c
> int F() {return 0;}
>      int G(int i) {return i;}
> ```

y.c:

> ```c
>     int F() {return 1;}
>      int G(int);
>      int main() {return G(0);}
> ```

because `F` is defined twice.
