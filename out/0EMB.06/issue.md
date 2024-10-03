Description: 7.18a.6.1 (fp arithmetic support functions) does not specify what
happens if an integer result overflows.

Proposed solution: Isn't there a blanket statement to the effect that when a
specified result is not representable in the type, the behavior is undefined? If
not, there should be.
