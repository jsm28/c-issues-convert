If no size information is known in the outer scope, then consider the following
example:

```c
extern int a[];
 int f() {
 extern int a[10];
 ...
 }
 int g() {
 extern int a[20]; /* error? */
 ...
 }
```

Is this legal? If not, does it violate a constraint?
