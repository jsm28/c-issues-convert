Gluing during rescan

Reference: subclause 6.8.3.3, page 90\. Does the rescan of a macro invocation
also perform gluing?

```c
#define hash_hash # ## #
 #define mkstr(a) # a
 #define in_between(a) mkstr(a)
 #define join(c, d) in_between(c hash_hash d)

 char p[2] = join(x, y);
```

Is the above legal? Does `join` expand to `"xy"` or `"x ## y"`?

It all depends on the wording in subclause 6.8.3.3 on page 90, lines 39-40. Does
the wording “... before the replacement list is reexamined ...” mean before
being reexamined for the first time only, or before being reexamined on every
rescan?

This rather perverse macro expansion is only made possible because the
constraints on the use of `#` refer to function-like macros only. If this
constraint were extended to cover object-like macros the whole question goes
away.

Dave Prosser says that the intent was to produce `"x ## y"`. My reading is that
the result should be `"xy"`. I cannot see any rule that says a created `##`
should not be processed appropriately. The standard does say in subclause
6.8.3.3, page 90, line 40 “... each instance of a `##` ...”

The reason I ask if the above is legal is that the order of evaluation of `#`
and `##` is not defined. Thus if `#` is performed first the result is very
different than if `##` goes first.
