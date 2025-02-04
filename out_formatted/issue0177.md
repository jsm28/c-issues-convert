## Issue 0177: A Preprocessing directives question

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather, BSI  
Date: 1995-10-16  
Submitted against: C90  
Status: Fixed  
Fixed in: C99  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_177.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_177.html)

*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 025: Preprocessing directives

Preprocessing directives are not removed from the translation unit at any point
during or after translation phase 4, and thus wreck the syntax analysis in
translation phase 7\.

Subclause 5.1.1.1 reads in part:

A source file together with all the headers and source files included via the
preprocessing directive `#include`, less any source lines skipped by any of the
conditional inclusion preprocessing directives, is called a *translation unit.*

Nothing here, in the description of translation phase 4, or in subclause 6.8,
states that any preprocessing directive is removed (except for `#include`, which
is *replaced*).

Consider the source file:

```c
#define QUIT return 0
 #if 0
 This is some junk
 #else
  int main (void)
 {
         puts ("Hello world\n");
 #endif
          QUIT;
 }
```

The translation unit resulting at the end of translation phase 4 is thus:

```c
#define QUIT return 0
 #if 0
 #else
 int main (void)
  {
         puts ("Hello world\n");
 #endif
         return 0;
 }
```

and this clearly does not match the syntax of *translation-unit* in subclause
6.7.

### Suggested Technical Corrigendum

In subclause 5.1.1.2, add at the end of the description of translation phase 4:
All preprocessing directives are then removed from the translation unit.
