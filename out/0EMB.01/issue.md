Description: by selecting the letter 'k' as suffix for the accum type, the the
function to convert a string to an accum type gets the name strtok; this name is
already in use in the C standard. Possible solutions:

* use a different letter
  + 'q' as proposed originally, conflicts with quadruple precision format
  + 'y' the only reasonable choice of the 'free' letters (others are 'b', 'm', 'v' and 'w');
* change the names of all "strto" functions to "strto\_"; that is: "strtok" becomes "strto\_k", "strtoht" becomes "strto\_hr", etc. Easy to do but a little bit inconsistent with the C library;
* use the letter 'q' only for the functionnames, leave the 'k' everywhere else.
