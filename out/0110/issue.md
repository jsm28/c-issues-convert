ANSI/ISO C Defect report #rfg17:

Subject: Formal parameters having array-of-non-object types.

a) For which (if any) of the following function declarations and definitions is
a diagnostic required?

b) Which (if any) of the following function declarations and definitions would,
if present in a translation unit, render the translation unit not strictly
conforming?

```c
typedef void VT;
 typedef struct incomplete_S ST;
 typedef union  incomplete_U UT;
 typedef int AT[];
 typedef void (FT) ();

 void declaration1 (VT arg[]);		/* ? */
 void declaration2 (ST arg[]);		/* ? */
 void declaration3 (UT arg[]);		/* ? */
 void declaration4 (AT arg[]);		/* ? */
 void declaration5 (FT arg[]);		/* ? */

 void definition1 (VT arg[]) { }	/* ? */
 void definition2 (ST arg[]) { }	/* ? */
 void definition3 (UT arg[]) { }	/* ? */
 void definition4 (AT arg[]) { }	/* ? */
 void definition5 (FT arg[]) { }	/* ? */
```

Footnote: I have heard rumors that the issue of the exact timing of the decay of
a formal parameter's array type into a pointer type (relative to the timing of
the necessary check that the type of the formal parameter is in fact a valid
type) was determined *explicitly* to be undefined by the Committee, but there is
no record of this in the CIB #1 document I have. \[CIB #1 is X3J11's earlier
attempt to respond to Defect Reports #001-#035, then called Requests for
Interpretation #001-#035.]

References: CIB #1, [RFI #13, question #1](issue:0013.01); CIB #1, [RFI #17,
question #14](issue:0017.14); CIB #1, [RFI #17, question #15](issue:0017.15)
