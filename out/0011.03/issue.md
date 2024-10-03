Initialization of tentative definitions

If the file scope declaration

```c
int i[10];
```

appears in a translation unit, subclause 6.7.2 suggests that it is implicitly
initialized as if

```c
int i[10] = 0;
```

appears at the end of the translation unit. However, this initializer is
invalid, since subclause 6.5.7 prescribes that the initializer for any object of
array type must be brace-enclosed. We believe that the intention of subclause
6.7.2 is that this declaration has an implicit initializer of

```c
int i[10] = {0};
```

Is this true?
