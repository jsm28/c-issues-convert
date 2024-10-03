In subclause 7.10.1.4 **The `strtod` function** page 151, line 5: What does
“`"C"` locale” mean?

a.

```c
setlocale(LC_ALL,NULL) == "C"
```

b.

```c
setlocale(LC_NUMERIC,NULL) == "C"
```

c. `&&`

d.

```c
||
```

e. something else.

What does “other than the `"C"` locale” mean?

a.

```c
setlocale(LC_ALL,NULL) != "C"
```

b.

```c
setlocale(LC_NUMERIC,NULL) != "Ct
```

c.

```c
&&
```

d.

```c
||
```

e. something else.

Subclause 7.4.1 **Locale control**, page 107 may help answer the questions.
