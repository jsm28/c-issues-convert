### Summary

I see several issues with **ATOMIC\_VAR\_INIT**. They could be turned into one
combined defect report, or separate defects, or folded into DR 422\.

Consider the following code:

```c
#include <stdatomic.h>
int main(void){
 atomic_int guide1 = ATOMIC_VAR_INIT(42); /* known value(42); WHAT STATE? */
 atomic_int guide2;        /* indeterminate value; indeterminate state */
 atomic_int guide3 = 42;   /* known value(42); indeterminate state */
static atomic_int guide4;  /* known value(0); valid state */
static atomic_int guide5 = 42; /* known value(42); valid state */
 atomic_int guide6;
 atomic_init(&guide6, 42); /* known value(42); initialized state */
 return 0;
}
```

What is the status of the additional state carried for guide1?

* Implicitly undefined
* Indeterminate
* Valid
* Initialized
* Something else

Is the state of guide1 the same as what guide6 has? If yes, does
"initialization-compatible" mean do the same thing as if atomic\_init() of the
same object with the same value?

* (Issue 5 from N1777)

  Zero initialization of static atomic objects in C requires more than in C\+\+.

  I have been told that C's 7.17.2.1#2:

  > ...; however, the default (zero) initialization for objects with static or
  > thread-local storage duration is guaranteed to produce a valid state.

  is not in C\+\+. If true and assuming that the two languages should be the
  "same" here, should this be deleted from C? Added to C\+\+?

  DR 422 is somewhat related to this issue.

### Suggested Technical Corrigendum

* No suggestion on the requirements mis-match between C and C\+\+.
