Assuming (b) is the correct interpretation of Question 3, if within a
translation unit at a point where an “integer constant expression” is required
to satisfy a language constraint \- such as to specify the size of a bit-field
member of a structure, the value of an enumeration constant, the size of an
array, or the value of a case constant \- does the use of the macro `offsetof`
constitute:

a. a constraint violation?

or

b. the use of undefined behavior, which renders the translation unit to be not
strictly conforming?
