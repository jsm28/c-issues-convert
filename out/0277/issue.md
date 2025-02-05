### Problem

Consider the code:

```c
  for (enum fred { jim, sheila = 10 } i = jim; i < sheila; i++)
        // loop body
```

6.8.5#3 reads:

> \[#3\] The declaration part of a `for` statement shall only declare identifiers
> for objects having storage class `auto` or `register`.

Does this wording forbid the declaration of tag `fred` \- since it is not an
object \- or is `fred` not covered by that wording because it is not an object ?

### Suggested Technical Corrigendum

Change 6.8.5#3 to one of:

> \[#3\] The declaration part of a `for` statement shall only declare identifiers
> for objects; any object so declared shall have storage class `auto` or
> `register`.

or:

> \[#3\] Any object whose identifier is declarared in the declaration part of a
> `for` statement shall have storage class `auto` or `register`.
