Is a compiler which allows the Relaxed Ref/Def linkage model to be considered a
conforming compiler? That is, can a compiler that compiles the following code
with no errors or warnings

```c
filea.c:
 #include stdio.h>
 void foo(void);
 int age;
 int main()
 {
 age = 24;
 printf("my age is %d.\n", age);
 foo();
 printf("my age is %d.\n", age);
 return 0;
 }

 fileb.c:
 #include <stdio.h>
 int age;
 void foo()
 {
 age = 25;
 printf("your age is %d.\n", age);
 }
```

and which produces the following output

```c
my age is 24
 your age is 25
 my age is 25
```

be called a standard-compliant compiler?
