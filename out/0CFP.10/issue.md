### Summary

This is about the issue raised by Joseph Myers in email SC22WG14.14358:

> TS 18661-1 gives the declaration of `fesetmode` as:
> 
> ```c
> int fesetmode(const fenv_t *modep);
> ```
> 
> The argument should be of type `const femode_t *`, not `const fenv_t *`.
> 
> \--

This was an editorial cut-and-past error. The Description says the argument
`modep` shall point to an objet set by a call to `fegetmode`, which sets objects
of type `femode_t`. It’s unlikely the function would be implemented with the
erroneous type.

### Suggested Technical Corrigendum

In 15.3, in the new text for C 7.6.3.1a#1, change:

```c
          int fesetmode(const fenv_t *modep);
```

to:

```c
          int fesetmode(const femode_t *modep);
```
