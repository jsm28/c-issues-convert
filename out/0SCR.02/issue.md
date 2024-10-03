### Summary

This suggestion comes from MISRA, as they are adding support for 17961 to their
rules.

Rule 5.40 names a number of functions that can attempt to write beyond the
bounds of the target array, if supplied with tainted input, namely: fscanf,
scanf, vfscanf, vscanf, sscanf, vsscanf and sprintf.

The observation is that vsprintf should be included in this list. Also the \_s
versions of all the above (including vsprintf\_s) should be included, as they
also can write beyond the end of the target array.

It is suggested that this is a defect rather than an enhancement, as from the
rationale for the rule, they should have been included when drafted.
