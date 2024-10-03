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
