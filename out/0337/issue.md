### Summary

The BUFSIZ macro is introduced in 7.19.1 para 3 as

> BUFSIZ  
> which expands to an integer constant expression that is the size of the buffer
> used by the setbuf function

There is no requirement that BUFSIZ should be a non-zero, positive integer
constant expression. Such a requirement should be spelled out clearly.

The same is true for FOPEN\_MAX and FILENAME\_MAX.

### Suggested Technical Corrigendum

Change the definition of BUFSIZ to:

> BUFSIZ  
> which expands to a non-zero, positive integer constant expression that is the
> size of the buffer used by the setbuf function

Similarly,

> FOPEN\_MAX  
> which expands to a non-zero, positive integer constant expression that is the
> minimum number of files that the implementation guarantees can be open
> simultaneously;
> 
> FILENAME\_MAX  
> which expands to a non-zero, positive integer constant expression that is the
> size needed for an array of char large enough to hold the longest file name
> string that the implementation guarantees can be opened;
