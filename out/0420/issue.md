### Summary

The standard lists two different forms for the `for`-statement in 6.8.5p1:

```c
for ( expression[opt] ; expression[opt] ; expression[opt] ) statement
for ( declaration expression[opt] ; expression[opt] ) statement
```

whereas later in 6.8.5.3 these two forms are subsumed in a third form by:

```c
for ( clause-1 ; expression-2 ; expression-3 ) statement
```

Obviously the second form above is a typo and doesn't fit within this third
form, the semantic that is given in 6.8.5.3 and to common practice in existing
compilers.

### Suggested Technical Corrigendum

Replace the second form in 6.8.5p1 and A.2.3 by the intended one:

```c
for ( declaration expression[opt] ; expression[opt] ; expression[opt] ) statement
```
