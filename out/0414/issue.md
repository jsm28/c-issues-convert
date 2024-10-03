### Summary

In 7.26.1 paragraph 5

> The enumeration constants are
> 
> > ```c
> > mtx_plain
> > ```
> 
> which is passed to `mtx_init` to create a mutex object that supports neither
> timeout nor test and return;

the "test and return" is referring to `try_lock`, `try_lock` is not optional,
therefore the "test and return" should be removed.   

In 7.26.4.2 paragraph 2

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of the six values:  
> `mtx_plain` for a simple non-recursive mutex,  
> `mtx_timed` for a non-recursive mutex that supports timeout,  
> `mtx_plain | mtx_recursive` for a simple recursive mutex, or   
> `mtx_timed | mtx_recursive` for a recursive mutex that supports timeout.

There are not **six** values listed, "six" should be changed to "these".

### Suggested Technical Corrigendum

Change 7.26.1 paragraph 5 to

> The enumeration constants are
> 
> > ```c
> > mtx_plain
> > ```
> 
> which is passed to `mtx_init` to create a mutex object that does not support
> timeout;

Change 7.26.4.2 paragraph 2 to

> The `mtx_init` function creates a mutex object with properties indicated by
> `type`,   
> which must have one of these values:
