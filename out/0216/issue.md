### Summary

The Standard is clear that the basic source character set need not have the same
encoding as the basic execution character set, and that while the latter must be
all positive, there is no such requirement on the former:

6.2.5:

> \[#3\] \[...\] If a member of the basic execution character set is stored in a
> char object, its value is guaranteed to be positive.

6.10.1:

> \[#3\] \[...\] Whether the numeric value for these character constants matches
> the value obtained when an identical character constant occurs in an expression
> (other than within a `#if` or `#elif` directive) is
> implementation-defined.<sup>141\)</sup> Also, whether a single-character
> character constant may have a negative value is implementation-defined.

However, there are two problems with this. Firstly, the cited wording in 6.2.5
conflicts with the definition of the basic execution character set:

5.2.1:

> \[#2\] \[...\] A byte with all bits set to 0, called the *null character*, shall
> exist in the basic execution character set; it is used to terminate a character
> string.

in that zero is not positive. Secondly, it is not clear whether a source
character constant can have the value zero; in other words, can:

```c
  #if !'A'
    #error Character A is zero
    #endif
```

reach the `#error` directive ?

### Suggested Technical Corrigendum

Change the cited wording in 6.2.5 to:

> #3\] \[...\] If a member of the basic execution character set (other than the
> null character) is stored in a char object, its value is guaranteed to be
> positive.

and the last part of the cited wording in 6.10.1 to:

> \[#3\] \[...\] Also, whether a single-character character constant may have a
> negative value is implementation-defined (nevertheless, it may not be zero).
