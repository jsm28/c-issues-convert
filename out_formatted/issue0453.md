## Issue 0453: Atomic flag type and operations

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Fred J. Tydeman (USA)  
Date: 2013-10-22  
Reference document: [N1776](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1776.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

It appears to me that there is a wording problem in 7.17.8.\*

> 7.17.8 Atomic flag type and operations  
> #1: The **atomic\_flag** type provides the classic test-and-set functionality.
> It has two states, set and clear.
>
> 7.17.8.1 The atomic\_flag\_test\_and\_set functions  
> #2: Atomically sets the value pointed to by **object** to true.
>
> #3: Atomically, the value of the object immediately before the effects.
>
> 7.17.8.2 The atomic\_flag\_clear functions  
> #2: Atomically sets the value pointed to by **object** to false.

An issue is states (set, clear) versus values (true, false).

Does an atomic\_flag structure have both states (set, clear) and values (true,
false)? Can it have all four combinations?

Another issue is 'set' is used both as a verb and a noun.

Another issue is: While the test is atomic, and the set is atomic, it is not
clear that both test and set are part of the same atomic operation.

I have been told that the same issues exists in the C\+\+ standard (29.7
\[atomics.flag]).

There was discussion of these topics on the WG14 reflector (around messages
13067 to 13073\)

One person in the discussion would like the value zero (from default static
initialization) to be the clear state. They also mentioned DR 421\.

Based upon the email discussion, the intent was that flags logically have
exactly two states: "set" and "clear". The test\_and\_set operation returns true
if it was "set", and false if it was "clear". Test\_and\_set sets the state to
"set", and the clear operations set the state to "clear". The value zero need
not be the "clear" state.

### Suggested Technical Corrigendum

Replace

> 7.17.8.1 The atomic\_flag\_test\_and\_set functions  
> #2: Atomically sets the value pointed to by **object** to true.
>
> #3: Atomically, the value of the object immediately before the effects.
>
> 7.17.8.2 The atomic\_flag\_clear functions  
> #2: Atomically sets the value pointed to by **object** to false.

with:

> 7.17.8.1 The atomic\_flag\_test\_and\_set functions  
> #2: Tests the state of the flag pointed to by **object** and then sets the flag,
> as a single atomic operation.
>
> #3: Returns true if the flag was set when tested or false otherwise.
>
> 7.17.8.2 The atomic\_flag\_clear functions  
> #2: Atomically clears the flag pointed to by **object**.

Add to the rationale in the section on atomic flag:

> The atomic flag type is defined in terms of states, not values, as the value
> zero (false) need not be the "clear" state. The committee knows of one
> implementation where zero is the "set" state.

---

Comment from WG14 on 2017-11-03:

Apr 2014 meeting

### Committee Discussion

* The committee agrees that the use of *true* and *false* are inaccurate.
* The committee does not feel that the proposed words are a sufficient resolution, however, and has solicited a new paper to resolve the issue.

Oct 2014 meeting

### Committee Discussion

> The paper [N1853](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1853.htm)
> was provided and discussed, revised, discussed further, and a further paper was
> solicited. In particular, the committee did not like "converted to a \_Bool"
> because it implies some unspecified arithmetic conversion.

Apr 2015 meeting

### Committee Discussion

> The paper [N1908](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1908.pdf)
> was provided and discussed. "Clears" the flag was vaguely troubling and a new
> approach was offered:
>
> > In 7.17.8.1p2, change:
> >
> > Atomically sets the value pointed to by `object` to true.
> >
> > to:
> >
> > Atomically places the atomic flag pointed to by `object` in the set state and
> > returns the value corresponding to the immediately preceding state.
> >
> > In 7.17.8.1p3, change:
> >
> > Atomically, the value of the object immediately before the effects.
> >
> > to:
> >
> > The `atomic_flag_test_and_set` functions return the value that corresponds to
> > the state of the atomic flag immediately before the effects. The return value
> > true corresponds to the set state and the return value false corresponds to the
> > clear state.
> >
> > In 7.17.8.2p2, change:
> >
> > Atomically sets the value pointed to by `object` to false.
> >
> > to:
> >
> > Atomically places the atomic flag pointed to by `object` into the clear state.

Oct 2015 meeting

### Committee Discussion

> The direction developed late at the last meeting is adopted as the Proposed
> Technical Corrigendum.

### Proposed Technical Corrigendum

In 7.17.8.1p2, change:

> Atomically sets the value pointed to by `object` to true.

to:

> Atomically places the atomic flag pointed to by `object` in the set state and
> returns the value corresponding to the immediately preceding state.

In 7.17.8.1p3, change:

> Atomically, the value of the object immediately before the effects.

to:

> The `atomic_flag_test_and_set` functions return the value that corresponds to
> the state of the atomic flag immediately before the effects. The return value
> true corresponds to the set state and the return value false corresponds to the
> clear state.

In 7.17.8.2p2, change:

> Atomically sets the value pointed to by `object` to false.

to:

> Atomically places the atomic flag pointed to by `object` into the clear state.
