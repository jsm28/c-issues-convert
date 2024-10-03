### Summary

The C11 specification of mutexes is missing the total order over all the calls
on a particular mutex. This is present in C\+\+11. The following is from
30.4.1.2p5 in
[N3291](https://www.open-std.org/jtc1/sc22/wg21/prot/14882fdis/n3291.pdf):

> For purposes of determining the existence of a data race, these behave as atomic
> operations (1.10). The lock and unlock operations on a single mutex shall appear
> to occur in a single total order. \[ Note: this can be viewed as the
> modification order (1.10) of the mutex. — end note ]

The synchronisation in 7.26.4 is defined in terms of some order over these
calls, even though none is specified, for instance 7.26.4.4p2 reads:

> Prior calls to mtx\_unlock on the same mutex shall synchronize with this
> operation.

This seems like simple omission. We suggest adding a new paragraph to 7.26.4
that matches C\+\+11:

> For purposes of determining the existence of a data race, mutex calls behave as
> atomic operations. The lock and unlock operations on a single mutex shall appear
> to occur in a single total order.
> 
> *NOTE:* This can be viewed as the modification order of the mutex.

### Suggested Technical Corrigendum

See above.
