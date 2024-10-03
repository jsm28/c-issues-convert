When is `sizeof` needed?

Refer to subclause 6.5.2.3, page 62, lines 28-29. When is the size of an
incomplete structure needed? An interpreter may not need the size until run
time, while some strictly typed memory architecture may not even allow pointers
to structures of unknown size.

In subclause 6.5.2.3, Footnote 63 starts off as an example. The last sentence
contains a “shall.” Does a violation of this “shall” constitute undefined
behavior?

Even though an interpreter may not need the size of a structure until run time
its compiler still has to do some checking, i.e. an unexecuted statement may
contain `sizeof` an incomplete type; even though the statement is unexecuted the
constraint still has to be detected.
