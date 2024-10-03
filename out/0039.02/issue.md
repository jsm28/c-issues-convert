I also would like to make a requirement that if the current locale is the `"C"`
locale, the value returned by `setlocale(LC_ALL, NULL)` be a string of length
one, consisting of the single character `C`.

Currently the value of `setlocale(LC_ALL, NULL)` is unspecified for the `"C"`
locale.

This makes it difficult to build libraries where you want to maintain the
behavior pre-existing to internationalization for backward compatibility.

Typically you want to say in these programs:

```c
if (*setlocale(LC_ALL, NULL) == 'C')
 do the old thing
 else
 do the new thing
```
