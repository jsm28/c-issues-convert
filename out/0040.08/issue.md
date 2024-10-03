Refer to subclause 6.1.2.5, page 22, lines 32-36:

a.

```c
char c = 7; /* implementation defined behavior, since 7 need not
 be a member of the basic execution character set */
```

b.

```c
c = 'a'; /* ok */
 c++; /* implementation defined */
```

c.

```c
c = '1'; /* ok */
 c++; /* ok? */
```

It has been suggested that the above constructs are not implementation defined.

Subclause 6.1.3.4, page 29, lines 30-33:

d.

```c
c = '\07'; /* what is in the source/execution character set is
 given in subclause 5.2.1. Anything else is an extension. */
```

e.

```c
c = '$';
```

It has been suggested that characters may be added to the basic source/execution
character set without implementation defined behavior being invoked. (I guess my
position on this item can be deduced from the text.)
