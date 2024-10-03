Item 14 \- stability of addresses

Is the address of an object constant throughout its lifetime? For example, if a
pointer to an object is written to a binary file using `fwrite`, and then read
back later during the same run of the program using `fread`, is it guaranteed to
compare equal to the address of the original object taken again?
