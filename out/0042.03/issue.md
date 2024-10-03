Similar questions arise for the other library string handling functions that
have undefined behavior when copying between overlapping objects. These include
`strcpy`, `strncpy`, `strcat`, `strncat`, `strxfrm`, `mbstowcs`, `wcstombs`,
`strftime`, `vsprintf`, `sscanf`, and `sprintf`. For these functions, however,
the number of bytes referenced through each pointer depends, at least in part,
upon the values stored in the bytes.

Consider a library function for which the number of bytes accessed or modified
is affected by the values of the bytes. Is the object associated with each of
its pointer arguments the smallest contiguous sequence of bytes actually
accessed or modified through that pointer?

In Example 4:

```c
void f4(void) {
        extern char b[2*N];
        strcpy(b+N, b);
        }
```

is the behavior defined if `N >> strlen(b)`?

In Example 5:

```c
void f5(void) {
        extern char c[2*N];
        strcat(c+N, c);
        }
```

is the behavior defined if both `N >> strlen(c)` and `N >> strlen(c) +
strlen(c+N)`?
