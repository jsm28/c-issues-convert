Tentative definition of externally-linked object with incomplete type

If one writes the file-scope declaration

```c
int i[];
```

then subclause 6.7.2 suggests that at the end of the translation unit the
implicit declaration

```c
int i[] = {0};
```

or equivalently

```c
int i[1] = {0};
```

appears. This seems peculiar, since subclause 6.7.2, (page 83, lines 35-36)
specifically forbids this case for internally linked identifiers.

Is this what is intended?
