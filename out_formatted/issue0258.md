## Issue 0258: ordering of "defined" and macro replacement

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Clive D.W. Feather \<clive@demon.net\>, UK C Panel  
Date: 2001-09-07  
Submitted against: C99  
Status: Closed  
Converted from: [summary-c99.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/summary-c99.htm), [dr_258.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_258.htm)

### Problem

Consider the code:

```c
  #define repeat(x) x && x    // Line 1   #if repeat(defined fred)    // Line 2
```

and the code:

```c
  #define forget(x) 0         // Line 3   #if forget(defined fred)    // Line 4
```

6.10.1#3 says:

> \[#3] Prior to evaluation, macro invocations in the list of preprocessing tokens
> that will become the controlling constant expression are replaced (except for
> those macro names modified by the `defined` unary operator), just as in normal
> text. If the token `defined` is generated as a result of this replacement
> process or use of the `defined` unary operator does not match one of the two
> specified forms prior to macro replacement, the behavior is undefined.

Does line 2 "generate" a `defined` operator ? Is line 4 strictly conforming
code, or does the fact that macro expansion "forgets" the `defined` operator
cause a problem ?

The restriction was clearly intended to make code like the following undefined:

```c
   #define jim defined
    #if jim loves sheila
```

I would guess that the original intention was that any `defined X` pair in the
original source worked correctly. The proposed change would resolve this.

In addition, given the order of events, it is unsuitable to say that a `defined
X` expression is "evaluated". Rather it should be described as a textual
substitution.

### Suggested Technical Corrigendum

Change 6.10.1#1 to read:

> \[...]
>
> ```c
>      defined identifier
> ```
>
> or
>
> ```c
>      defined ( identifier )
> ```
>
> which are replaced by the token `1` if the identifier is currently  
> \[...]  
> subject identifier), or the token `0` if it is not.

and #3 to read:

> \[#3] Prior to evaluation, the list of preprocessing tokens that will become the
> controlling constant expression is examined. Firstly all expressions using the
> `defined` operator are replaced as described above, and then macro invocations
> are replaced, just as in normal text. If the token `defined` appears in the list
> after the replacement process, or the use of the `defined` unary operator does
> not match one of the two specified forms prior to macro replacement, the
> behavior is undefined. After all \[...]

---

Comment from WG14 on 2002-03-06:

### Committee Response

The standard does not clearly specify what happens in this case, so portable
programs should not use these sorts of constructs.
