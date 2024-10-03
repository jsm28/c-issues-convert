Description: The type-generic macro definition sections (2.1.7.6 and 7.18a.6.7)
are incomplete and possibly wrong.

Incomplete because there are no rules on which function should be called when a
type- generic macro is called with a non fixed-point type argument. Possibly
wrong, because it is not clear what the name of the type-generic macro's should
be: 2.1.7.6 suggest to call the type-generic abs function 'absfx', in 7.18a.6.7
the 'fx' part of the name is in italic which might suggest that the name should
really be 'abs'. So, do we want to have 'abs', 'round' and 'countls', or
'absfx', 'roundfx' and 'countls'?

Proposed solution:
