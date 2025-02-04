## Issue 0EMB.08: Diagnostic required on named-register constraint violation?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14  
Date: 2004-09-23  
Reference document: Embedded-c email list [208](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/208), [210](https://www.open-std.org/jtc1/sc22/wg14/embedded-c/210)  
Submitted against: Embedded C TR 18037:2004  
Status: Fixed  
Fixed in: Embedded C TR 18037:2008  
Converted from: [n1071.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1071.pdf), [n1087.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1087.pdf), [n1180.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1180.pdf)

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

---

Comment from WG14 on 2004-11-15:

Problem: Consider

```c
// file 1
register REG_A int reg_a;

// file 2
extern int reg_a;
int main() { return reg_a; }
```

According to the second new constraints for 6.7.1 this is not allowed:

> If an object is declared with a named-register storage-class specifier, every
> declaration of that object shall include the same named-register storage-class
> specifier.

The 'shall' implies that a diagnostic is required here. However, so far C
compilers have not been required to diagnose such issues across translation
units. Is this really the intention?

Solution: The intent is to require a diagnostic for different named-register
storage-class specifier declarations within a single translation unit for the
same object.

Changes:

* Change in the second of the new constraint paragraphs for 6.7.1 the words 'every declaration of that object' to 'every declaration of that object within the same translation unit'.
* In the new text for 6.7.1.1, add at the beginning of the last paragraph (paragraph 6\) the sentence: 'If an object is declared with a named-register storage-class specifier, every declaration of that object shall include the same named-register storage-class specifier.'
