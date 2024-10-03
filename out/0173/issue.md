*Submitted to BSI by Clive D.W. Feather clive@sco.com .*

*In this Defect Report, identifiers lexically identical to those declared in
standard headers refer to the identifiers declared in those standard headers,
whether or not the header is explicitly mentioned.*

*This Defect Report has been prepared with considerable help from Mark Brader,
Jutta Degener, Ronald Guilmette, and a person whose employment conditions
require anonymity. However, except where stated, opinions expressed or implied
should not be assumed to be those of any person other than myself.*

Defect Report UK 021: Line numbers

The concept of *line number* is not clearly defined when a token is split over
more than one physical source line.

Subclause 6.8.4 reads in part:

The line number of the current source line is one greater than the number of
new-line characters read or introduced in translation phase 1 (5.1.1.2) while
processing the source file to the current token.

Subclause 6.8.8 reads in part:

`__LINE__` \- The line number of the current source line (a decimal constant).

Consider the program:

```c
#include  stdio.h
 #define LNER __LINE__

 /* The next statement is on physical source lines 6 to 8 */
 int east_coast = __\
 LINE\
 __;
 /* The next statement is on physical source lines 10 to 13 */
 int main_line = L\
 N\
 E\
 R;

 int main (void)
 {
         printf ("%d %d\n", east_coast, main_line);
         return 0;
 }
```

In each of the two substitutions, it is unclear whether the line number is the
number of new-lines read to the *start of* the current token, or to the *end of*
the current token, or to a specified point within the current token.

What is the output of this program?
