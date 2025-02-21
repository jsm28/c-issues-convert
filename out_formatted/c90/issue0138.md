## Issue 0138: What are the storage durations?

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: John Max Skaller, Project Editor (P.J. Plauger)  
Date: 1994-06-02  
Submitted against: C90  
Status: Fixed  
Fixed in: C90 TC2  
Converted from: [dr.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr.htm), [dr_138.html](https://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_138.html)

Subclause 6.1.2.4 says:

> An object has a *storage duration* that determines its lifetime. There are two
> storage durations: static and automatic.

To me that clearly excludes heap objects. Is there a Defect Report on that? If
so which one? (I have responses to Defect Report #001 through Defect Report
#059.) If not and something else in the Standard fixes it, can you point out
where?

---

Comment from WG14 on 1997-09-23:

### Correction

***In subclause 6.1.2.4, page 22, first paragraph, change:***

There are two storage durations: static and automatic.

***to:***

There are three storage durations: static, automatic, and allocated. Allocated
storage is described in 7.10.3.
