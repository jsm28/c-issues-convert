### Summary

In subclause 7.23.3.5p7, the specifications for the `strftime %c`, `%p`, and`%x`
conversion specifiers in the C locale conflict with the specifications in
ISO/IEC 9945-2 for the POSIX locale.  As the POSIX and C locales have always
been intended to be compatible, we strongly suggest changing these
specifications to match the pre-existing POSIX specifications.

### Suggested Correction

In subclause 7.23.3.5, paragraph 7, page 345, change the definitions of `%c`,
`%p`, and `%x` to:

> `%c`
> 
> > equivalent to "`%a %b %e %T %Y`".
> 
> `%p`
> 
> > one of "`AM`" or "`PM`".
> 
> `%x`
> 
> > equivalent to "`%m/%d/%y`".
