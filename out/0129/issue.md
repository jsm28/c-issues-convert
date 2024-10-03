ANSI/ISO C Defect Report #rfg36:

Subject: Tags and name spaces.

Should (or must) a conforming implementation correctly translate the following
code?

```c
void *vp;
 struct TAG { int i; };

 void f ()
        {
        enum TAG { enumerator };
        (struct TAG *) vp;
        }
```

Background:

Subclause 6.1.2.3 says:

> Thus, there are separate *name spaces* for various categories of identifiers, as
> follows:
> 
> ...
> 
> \- the *tags* of structures, unions, and enumerations (disambiguated by
> following any of the keywords `struct`, `union`, or `enum`);...

A footnote for this subclause states that “There is only one name space for tags
even though three are possible.”

Given that this statement is only a footnote, and given that there are neither
any specific constraints nor any specific semantic rules violated by the code
shown above, it appears that a conforming implementation is actually *required*
(by the C Standard, as now written) to accept the code shown above (even though
this was probably not the intent of the Committee). It also seems that the code
shown above is strictly conforming.

If the Committee actually intended that such code should be considered to be
invalid, then it seems necessary to amend the C Standard to make it say that.
(Actually, I think that a new constraint is in order here.)
