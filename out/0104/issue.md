ANSI/ISO C Defect report #rfg11:

According to subclause 6.5:

> If an identifier for an object is declared with no linkage, the type for the
> object shall be complete by the end of its declarator, or by the end of its
> init-declarator if it has an initializer.

It would appear that the above rule effectly renders the following code not
strictly conforming (because this code violates the above rule):

```c
typedef struct incomplete_S ST;
 typedef union  incomplete_U UT;

 void example1(ST arg); /* diagnostic permitted/encouraged? */
 void example2(UT arg); /* diagnostic permitted/encouraged? */
```

I have noted however that many/most/all “conforming” implementations do in fact
accept code such as that shown above (without producing any diagnostics).

Is it the intention of the Committee that code such as that shown above should
be considered to be strictly conforming? If so, then some change to the wording
now present in subclause 6.5 is in order (to allow for such cases).
