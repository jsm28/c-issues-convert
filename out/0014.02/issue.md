X/Open Reference Number KRT3.159.2

Subclause 7.9.6.2 **The `fscanf` function** states:

> If end-of-file is encountered during input, conversion is terminated. If
> end-of-file occurs before any characters matching the current input directive
> have been read (other than leading white space, where permitted), execution of
> the current directive terminates with input failure; otherwise, unless execution
> of the current directive is terminated with a matching failure, execution of the
> following directive (if any) is terminated with an input failure.

How should an implementation behave when end-of-file terminates an input stream
that satisfies all conversion specifications that consume input but there is a
remaining specification request that consumes no input (e.g. `%n`)? Should the
non-input-consuming directive be evaluated or terminated with an input failure
as described above?
