## Issue 0482: Macro invocation split over many files

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman  
Date: 2015-06-23  
Reference document: [N1942](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1942.htm)  
Submitted against: C11 / C17  
Status: Closed  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Based upon my reading of the standard, it appears that the following is strictly
conforming code. However, many compilers refuse to translate it (which I think
is good).

main.c:

```c
#include <string.h>  /* strcpy(), strcmp() */
#undef NDEBUG
#include <assert.h>  /* assert() */

int main(void) {
  int line1;
  int line2;
  char file1[1023];
  char file2[1023];

  #include "file1.h"    /* start of call of assert() split over many files */
  );                    /* end of assert() */

  assert( 2 == line1 );
  assert( 3 == line2 );
  assert( 0 != strcmp( file1, file2 ) );

  return 0;
} /* end main() */
```

file2.h:

```c
assert(
       ( (void)strcpy(file1,__FILE__), line1 = __LINE__ )
```

file1.h:

```c
#include "file2.h"
!=
  ( (void)strcpy(file2,__FILE__), line2 = __LINE__ )
```

There already are some ways to have a macro invocation be split over two files
that result in undefined behaviour.

5.1.1.2 Translation phases, paragraph 1, bullet 2 has:

> A source file that is not empty shall end in a new-line character, which shall
> not be immediately preceded by a backslash character before any such splicing
> takes place.

which makes using line splicing (as a way to split a macro invocation over many
files) undefined.

6.10.3 Macro replacement, paragraph 11 has:

> If there are sequences of preprocessing tokens within the list of arguments that
> would otherwise act as preprocessing directives,172) the behavior is undefined.

which makes using #include of arguments (as a way to split a macro invocation
over many files) between the outside-most matching parentheses undefined.

### Suggested Technical Corrigendum

Add to 5.1.1.2, paragraph 1, bullet 3, words along the lines of:

> A macro invocation shall be contained within one source file.

---

Comment from WG14 on 2017-04-07:

Oct 2015 meeting

### Committee Discussion

> The committee was unsympathetic to the Suggested Technical Corrigendum. It was
> noted that function invocations are allowed to span files and that there are
> some implementations that do support macro invocations that the Suggested
> Technical Corrigendum would invalidate.
>
> The committee agrees that such uses should probably have been prohibited in the
> original specification and may consider adding such restrictions in a possible
> future revision of the Standard, and will record this intent in the next
> revision of WG 14 Standing Document 3 currently at
> [N1972](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1972.htm) .

Apr 2016 meeting

### Committee Discussion

> The Proposed Committee Response was augmented.

### Proposed Committee Response

> The committee agrees that such uses should probably have been prohibited in the
> original specification and may consider adding such restrictions in a possible
> future revision of the Standard, and has recorded this intent in WG 14 Standing
> Document 3\.
>
> Although the committee agrees that such invocations are not necessarily best
> practice, they are supported in existing implementations and as such the
> committee sees no benefit to accepting changes that would invalidate this
> practice.
