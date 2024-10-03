I can find no prohibition of the following translation unit:

```c
struct foo x;
 struct foo { int i; };
```

What I was looking for, but didn't find, was a statement that an implicitly
initialized declaration of an object with static storage duration must have
object type. Is this translation unit legal?
