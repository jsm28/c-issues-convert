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

* (Issue 3 from N1777)

  **ATOMIC\_VAR\_INIT** is not usable in assignment to an atomic object.

  I see no difference between:

  ```c
  atomic_int guide = ATOMIC_VAR_INIT(42);
  ```

  and

  ```c
  atomic_int guide;
  guide = ATOMIC_VAR_INIT(42);
  ```

  I would hope that initialization (which looks like an assignment in a
  declaration) and a simple assignment would be equivalent and
  **ATOMIC\_VAR\_INIT** could be used in either context.
* (Issue 4 from N1777)

  What should happen if **ATOMIC\_VAR\_INIT**(value) is used in context other than initializing an atomic object of the same type as the value?

  Should it be undefined behaviour? A constraint violation? Just the value
  **value** converted to the type of the object?

  ```c
  atomic_float f = ATOMIC_VAR_INIT(42); /* type mis-match */

  int nonAtomic = ATOMIC_VAR_INIT(42); /* non-atomic object */

  if( ATOMIC_VAR_INIT(42) ){...};
  guide1 = 1729 + ATOMIC_VAR_INIT(42) * 3;

  void func( atomic_int ai ); /* function parm/arg */
  func( ATOMIC_VAR_INIT(42) ); /* DR 427 is now making this
                               initialization (not assigment) */
  ```

  DR 427 is changing how a function parameter is getting its value from the actual
  argument from assignment to initialization (to get around const). Would this
  initialization be a valid context for **ATOMIC\_VAR\_INIT**?

### Suggested Technical Corrigendum

* In the first sentence of 7.17.2.1#2, after

  > suitable for initializing

  add the words

  > or assigning to
* Add to 7.17.2.1 as a constraint or a new paragraph between 3 and 4:

  > If **ATOMIC\_VAR\_INIT** is used in a context other than initialization \[or
  > assignment\] of an atomic object of a compatible type of the value, the
  > behaviour is undefined.
