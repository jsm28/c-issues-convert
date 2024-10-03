I am requesting an interpretation of white space in the format string of a scan
statement. One of our customers is concerned about this as it appears to
conflict with some books on C. I am referring to subclause 7.9.6.2, page 135,
paragraph 3:

> A directive composed of white space character(s) is executed by reading input up
> to the first non-white-space character (which remains unread), or until no more
> characters can be read.

Page 135, paragraph 7 says:

> If the length of the input item is zero, the execution of the directive fails:
> this condition is a matching failure, unless an error prevented input from the
> stream, in which case it is an input failure.

My questions are:

1. Is white space in the format string a directive which must be satisfied by white space in the input string?
2. What are the correct answers to the following examples? Note the white space in the format string.

Example 1:

```c
inputString = "123ABCD";
 numAssigned = sscanf(inputString, "%lu %ls", &ulongVal, junkchar);
```

Should the result be `numAssigned` equal to 1?

Example 2:

```c
inputString = "123ABCD";
 numAssigned = sscanf(inputString, "%lu%ls", &ulongVal, junkchar);
```

Should the result be `numAssigned` equal to 2?
