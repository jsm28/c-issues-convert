### Summary

7.17.7.4 The atomic\_compare\_exchange generic functions  

7.17.7.4p2 Description  

  Atomically, compares the value pointed to by **object** for equality with  
  that in **expected**, and if true, replaces the value pointed to by **object**  
  with **desired**, and if false, updates the value in expected with the  
  value pointed to by **object**.  

When **object** is an atomic struct type and **expected** is the corresponding  
non-atomic struct type.  What does it mean to compare two struct types  
as equal?  

Where does the C standard define what it means for two objects of struct  
type to be equal?  

7.17.7.4 NOTE 1 gives an example using memcmp on how the test for  
equality might be defined.  But that is non-normative.  

But the padding bytes in a struct have unspecified values (6.2.6.1p6)  

7.24.4.1 The memcmp function, footnote 310 reminds us that the contents  
of padding in a struct is indeterminate.  

Even integers can have padding bits, whose values are unspecified (6.2.6.2p1)  

A similar issue probably occurs for Atomic union types.

### Suggested Technical Corrigendum

Either define equality of objects of struct type, add a restriction disallowing  
use of atomic structs as arguments for the atomic\_compare\_exchange generic
functions,  
or note that atomic\_compare\_exchange generic functions for objects of atomic  
struct type results in undefined behavior.
