## Issue 0103: Is a diagnostic required when formal parameters for functions are incomplete types?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Ron Guilmette, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_103.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_103.html)

ANSI/ISO C Defect report #rfg10:

According to subclause 6.5:

> If an identifier for an object is declared with no linkage, the type for the
> object shall be complete by the end of its declarator, or by the end of its
> init-declarator if it has an initializer.

Note that this rule appears in a **Semantics** section, so it would seem that
comforming implementations are permitted but not strictly required to produce
diagnostics for violations of this rule.

Anyway, my interpretation of the above rule is that conforming implementations
are permitted (and even encouraged it would seem) to issue diagnostics for code
such as the following, in which formal parameters for functions (which, by
definition, have no linkage) are declared to have incomplete types:

```c
typedef int AT[];

 void example1 (int arg[]);	/* diagnostic permitted/encouraged? */
 void example2 (AT arg);		/* diagnostic permitted/encouraged? */
```

I believe that subclause 6.5 needs to be reworded so as to clarify that code
such as that shown above is perfectly valid, and that conforming implementations
should not reject such code out of hand.

---

Comment from WG14 on 1997-09-23:

### Response

The types of the parameters are rewritten, as in subclause 6.7.1 via subclause
6.5.4.3. No incomplete object types are involved.
