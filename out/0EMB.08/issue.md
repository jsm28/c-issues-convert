Description: consider

```c
// file 1
register REG_A int reg_a;

// file 2
extern int reg_a;

int main() { return reg_a; }
```

According to the new constraints for 6.7.1 this is not allowed:

> If an object is declared with a named-register storage-class specifier, every
> declaration of that object shall include the same named-register storage-class
> specifier.

The 'shall' implies that a diagnostic is required here. However, so far C
compilers have not been required to diagnose such issues across translation
units. Is this really the intention?

Proposed solution:
