## Issue 0307: 6.10.3p10: Clarifiying arguments vs. parameters

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG21, WG21  
Date: 2004-10-26  
Reference document: [ISO/IEC WG14 N1068](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1068.htm)  
Submitted against: C99  
Status: Fixed  
Fixed in: C99 TC3  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_307.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_307.htm)

### Summary

Obviously, what appear in the definition syntax of a function-like macro are not
its arguments, but its parameters. On the other hand, what is similar
syntactically to a function call is obviously the invocation of the macro, not
its definition. Clearly, there is confusion about whether this sentence is
talking about the definition or an invocation.

Perhaps it would be clearer yet to say something like, "a function-like macro
<u>which takes</u> arguments, similarly syntactically to a function call".

### Suggested Technical Corrigendum

Change 6.10.3p10:

> A preprocessing directive of the form
>
> > `# define` *identifier lparen identifier-list<sub>opt</sub>* `)`
> > *replacement-list new-line*  
> > `# define` *identifier lparen* `... )` *replacement-list new-line*  
> > `# define` *identifier lparen identifier-list* `, ... )` *replacement-list
> > new-line*
>
> defines a function-like macro with ~~arguments~~ <u>parameters</u>, similar
> syntactically to a function call.

---

Comment from WG14 on 2006-03-05:

### Technical Corrigendum

Change 6.10.3p10:

> A preprocessing directive of the form
>
> > `# define` *identifier lparen identifier-list<sub>opt</sub>* `)`
> > *replacement-list new-line*  
> > `# define` *identifier lparen* `... )` *replacement-list new-line*  
> > `# define` *identifier lparen identifier-list* `, ... )` *replacement-list
> > new-line*
>
> defines a function-like macro with ~~arguments~~ <u>parameters</u>, <u>whose use
> is</u> similar syntactically to a function call.
