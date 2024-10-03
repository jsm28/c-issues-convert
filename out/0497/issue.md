### Summary

"white-space character" is defined differently in two places in the standard.

white-space character is defined in 6.4 as:

> space, horizontal tab, new-line, vertical tab, form-feed

standard white-space character is defined in 7.4.1.10 for **isspace()** as:

> space, horizontal tab, new-line, vertical tab, form-feed, carriage return

One place it matters is 7.21.6.2 fscanf().

7.21.6.2 fscanf() in paragraph 5 talks about white-space character(s) in the
directive. Since there is no reference to **isspace**, it must be referring to
6.4 (which I believe is wrong).

Paragraph 8, in the same section, talks about input white-space characters, but
refers to **isspace**.

In the following code, the \\r (carriage return) is a directive:

```c
#include  <stdio.h>
int main(void){
  static int rc, cnt1, cnt2, i;
  rc = sscanf( " 123", "\r%n%i%n", &cnt1, &i, &cnt2);
  printf("rc=%i, cnt1=%i, i=%i, cnt2=%i\n", rc, cnt1, i, cnt2);
  return 0;
}
```

Is the \\r a white-space character or an ordinary multibyte character?

By 5.2.1#3, the \\r is part of the basic execution character set, but is not
part of the basic source character set (as Doug Gwyn pointed out in message
14152).

By 6.4#3, the \\r is not a white-space character.

By 7.21.6.2#3, #5 and #6, since the \\r is not a white-space character, it is an
ordinary multibyte character. Therefore, since the \\r does not match the
characters of the stream, cnt1, i, and cnt2 are not altered. However, this not
what most implementations do. They output: rc\=1, cnt1\=1, i\=123, cnt2\=4

I see a mismatch between what implementations are doing and what the standard
requires.

Another issue is "white space" in 7.21.6.2#15. It should be "white-space
characters". Section 6.4 defines "white space" as both comments and white-space
characters. So, the use of "white space" in 7.21.6.2#15 would cause /\* comments
\*/ to be matched. The same issue applies to 7.29.2.2#15, 7.29.4.1.2#4,
7.22.1.4#4.

Another issue is "white-space wide character" is not well defined (in
7.30.2.1.10) and is missing from the index. Does the "C" locale matter?

### Suggested Technical Corrigendum

There are several ways this basic issue can be addressed.

1. Add 'carriage return' to the definition of white-space in 6.4. However, this only makes 6.4 and **isspace** match for the "C" locale.
2. Add '(as specified by the **isspace** function)' to 'white-space characters' throughout clause 7 of the standard. Add '(as specified by the **iswspace** function)' to 'white-space wide characters' throughout clause 7\.
3. Throughout clauses 5 and 6 (except for 5.1.1.2#7 which is execution), change 'white-space characters' to 'source white-space characters'. There might be an issue with 'non-white-space character' being changed to 'non-source-white-space character'.
   
   In clause 7.1.1, add definitions of 'execution white-space character' and
   'execution white-space wide character'. Change 'white-space character' to
   'execution white-space character' throughout clause 7\. Change 'white-space wide
   character' to 'execution white-space wide character' throughout clause 7\.
   
   Throughout clause 7, remove '(as specified by the **isspace** function)' and
   '(as specified by the **iswspace** function)'.
4. In (perhaps) 7.1.1, add something along the lines of:
   > In this clause, references to "white-space character" refer to execution
   > white-space character as defined by **isspace()**. References to "white-space
   > wide character" refer to execution white-space wide character as defined by
   > **iswspace()**.
   
   Throughout clause 7, remove '(as specified by the **isspace** function)' and
   '(as specified by the **iswspace** function)'.

Some of the above changes also require corresponding changes to Annexes A and J.

Also do these changes:

1. In 7.21.6.2#15, 7.29.2.2#15, 7.29.4.1.2#4, change "white space" to "white-space characters".
2. Give a better definition of "white-space wide character" in 7.30.2.1.10 with respect to "C" locale.
3. Add "white-space wide character" to the index.
