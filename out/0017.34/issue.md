Calls to `strtok`

In subclause 7.11.5.8 on page 167, line 36, “... first call ...” should read
“... all calls ...”

I think that the current wording causes confusion. The first call is the one
that takes a non-`NULL` “`s1`” parameter. However, the discussion from line 36
onwards is describing the behavior for all calls.
