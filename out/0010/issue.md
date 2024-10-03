Consider:

```c
typedef int table[];        /* line 1 */

 table one = {1};        /* line 2 */

 table two = {1, 2};     /* line 3 */
```

First, is the typedef to an incomplete type legal? I can't find a prohibition in
the standard. But an incomplete type is completed by a later definition, such as
line 2, so what is the status of line 3?

The type, of which `table` is only a synonym, can't be completed by line 2 if it
is to be used in line 3\. And what is `sizeof(table)`? What old C compilers seem
to do is treat the typedef as some sort of textual equivalent, which is clearly
wrong.
