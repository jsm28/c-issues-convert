## Issue 0130: When is data read from a text stream guaranteed to match what was written to the stream?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Sheng Yu, WG14  
Date: 1993-12-03  
Submitted against: C90  
Status: Closed  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_130.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_130.html)

Under subclause 7.9.2 **Streams**, page 125, lines 26-28:

> Data read in from a text stream will necessarily compare equal to the data that
> were earlier written out to the stream only if: the data consist only of
> printable characters and the control characters horizontal tab and new-line; ...

Writing on a text stream might not cause characters to be overwritten exactly
one for one, especially on fixed-length record based file systems. If the file
is not truncated beyond the point where the data is written, there is no sure
way to predict what will be read in after writing in the middle of a text stream
because the data might just replace a character, a line, etc. Consider the
following example:

```c
#include <stdio.h>
 #include <string.h>
 int buf[99];
 unsigned int len;
 int main()
        {
        FILE *f = fopen("test data", "w");
        fwrite("abc\ndef\n", 8, 1, f);
        fseek(f, 0, SEEK_SET);
        fwrite("UWXYZ", 5, 1, f);
        fseek(f, 0, SEEK_SET);
        len = fread(buf, 1, 10, f);
        if (len == 8 && !memcmp(buf, "UWXYZef\n"))
 		;	/* Case 1: OK, acts like binary */
        else if (len == 5 && !memcmp(buf, "UWXYZ", 5))
 		;	/* Case 2: OK to truncate after write */
        else if (len > 5 && !memcmp(buf, "UWXYZ", 5))
              printf("len = %u, buf = %s\n", len, buf);
 			/* Case 3: Is this nonstandard? */
        else
              printf("This is obviously nonstandard.\n");
        }
```

Can a conforming implementation translate the above program and produce the
following output (Case 3)?

```c
len = 9, buf = UWXYZdef
```

---

Comment from WG14 on 1997-09-23:

### Response

Yes, a conforming implementation may produce the “Case 3” output. However, there
may be cases in some conforming implementations in addition to those shown in
your example, so the printout “obviously nonstandard” may be inappropriate.
