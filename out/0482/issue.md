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
