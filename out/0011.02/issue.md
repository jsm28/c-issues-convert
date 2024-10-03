Interpretation of `extern`

Consider the code:

```c
/* File scope */
 static int i;           /* declaration 1 */

 main()
 {
 extern int i;           /* declaration 2 */
 {
     extern int i;       /* declaration 3 */
 }
 }
```

A literal reading of subclause 6.1.2.2 says that declarations 1 and 2 have
internal linkage, but that declaration 3 has external linkage (since declaration
1 is not visible, being hidden by declaration 2). (This combination of internal
and external linkage is undefined by subclause 6.1.2.2, page 21, lines 27-28.)

Is this what is intended?
