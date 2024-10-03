### Summary

Context:

In a distributed development environment, the exact file name passed to the
compiler or preprocessor may vary from site to site. It is therefore desirable
to be able to set the file name as seen by `__FILE__` and elsewhere to a uniform
value. The mechanism to do this is the '`#line <num> "<string>"`' form of the
'`#line`' preprocessor directive. It is also necessary that such a directive
leave the line numbering sequence unchanged. Further, it is desirable that edits
that change the location of the directive in the source module should not
require modification to the directive and that comments embedded in the
directive likewise do not have to be accounted for.

Searches of the online literature show that a directive of the form '`#line
__LINE__ "string"`' is expected to have this property.

Despite this, at least one compiler/preprocessor does not allow this.

Technical argument:

The value substituted for the predefined macro '`__LINE__`' is specified in
6.10.8.1p1 as the presumed line number of the current source line. The presumed
line number is initially (6.10.4p2) the number of newline characters (or their
equivalent) seen in phase 1 of the translation process, plus 1, *at the time of
substitution*. (Note that this is *not* the same as the time of tokenization,
which is where the failing compilers make their mistake.) The mechanism for
transferring this count between phase 1 and phase 4, where macro substitution
takes place, is not specified, but may be presumed to exist and be reliable. (If
it were not, the `__LINE__` predefined macro would be useless.) That makes the
question 'when does the substitution take place?'

Macro substitution in directives is a separate issue from macro expansion in
code. It does *not* always take place. If and when it occurs depends on the
directive and the details of its form. That means the entire directive has to be
'in hand' in order to be evaluated, and that means, in turn, that the newline
that terminates the directive has to have been seen. The standard goes to some
length to specify the various directive forms and all include the terminating
newline in their specification.

Therefore, when a substitution is made for '`__LINE__`', its value should be the
line count following the end of the directive, which is the same as the line
number of next line in the source module. This is precisely the value that
produces the desired property of the '`#line __LINE__ "string"`' directive.

Correction requested:

While there is no need to change the standard's normative text, a note that
'`#line __LINE__ "string"`' and similar directives leaves line numbering
unchanged would both be educational and make misinterpretations more difficult.

### Suggested Technical Corrigendum

Append the following to footnote 177 in 6.10.8.1p1:

`#line __LINE__ "newfilename"` changes the presumed file name without changing
the presumed line number.
