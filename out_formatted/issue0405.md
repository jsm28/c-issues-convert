## Issue 0405: mutex specification not aligned with C\+\+11 on total order

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG 14, Batty  
Date: 2011-10-14  
Reference document: [N1584](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1584.pdf)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

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

---

Comment from WG14 on 2017-11-03:

Oct 2011 meeting

### Committee discussion

> * The quoted text was added to C\+\+11 after WG 14 voted out the FDIS in London.
> * The consensus was that this is probably an oversight, and should be changed along the lines that are recommended above.

Feb 2012 meeting

### Committee Discussion

> * The wording in the proposed wording is not correct, should read "shall occur" rather than "shall appear to occur."
> * No consensus reached on the words, Clark Nelson took action item to furnish words for the next meeting.

Oct 2012 meeting

### Committee Discussion

Add the following as 7.26.4 p1 and p2:

> For purposes of determining the existence of a data race, lock and unlock
> operations behave as atomic operations. All lock and unlock operations on a
> particular mutex occur in some particular total order.
>
> *NOTE:* This total order can be viewed as the modification order of the mutex.

Apr 2013 meeting

### Committee Discussion

Accept wording from Oct 2012 as proposed technical corrigendum

### Proposed Technical Corrigendum

Add the following as 7.26.4 p1 and p2:

> For purposes of determining the existence of a data race, lock and unlock
> operations behave as atomic operations. All lock and unlock operations on a
> particular mutex occur in some particular total order.
>
> *NOTE:* This total order can be viewed as the modification order of the mutex.
