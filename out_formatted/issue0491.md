## Issue 0491: Concern with Keywords that Match Reserved Identifiers

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: WG14, Douglas Walls  
Date: 2016-02-23  
Reference document: [N2000](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2000.htm)  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C17  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

Should a conforming program be allowed to use identifiers spelled with a leading
underscore followed by an uppercase letter that match the spelling of a keyword?  

The C committee has been adding keywords to the C standard spelled with a
leading underscore followed by an uppercase letter so that they will not
conflict with identifiers that are not already reserved to the implementation,
i.e. so existing programs that conform to the C standard are not impacted by
addition of new keywords in a new revision of the C standard.  

So the C standard spells keywords in two ways:

* Leading underscore followed by an uppercase letter
* Leading lowercase letter

7.1.2p4 provides restrictions on when macros with names lexically identical to
keywords can be defined, thus infering when macro names lexically identical to
keywords can be defined.  

As specified in 7.1.3, identifiers spelled with a leading underscore followed by
an uppercase letter are reserved to the implementation.  While those identifiers
beginning with a lowercase letter are not.  Thus, for example, a conforming
program can use `inline` as a macro name, but a conforming program cannot use
`_Noreturn` as a macro name.  

Though the C committee has added new keywords from the reserved identifier
namespace, the committee has not updated the rules about reserved identifiers. 
What I don't know is if that is intentional or an oversight, as I don't ever
remember discussing the issue from that perspective during a committee meeting.   

The issue came to my attention when I found some C standard headers defining
\_`Noreturn` as a macro because they knew it is an identifier reserved to the
implementation.  I was a bit surprised, as it required a otherwise conforming
program to `#undef _Noreturn` in order to use the \_`Noreturn` keyword as a
function specifier.  The macro in this case was expanding to a gcc like
attribute syntax recognized by the compiler.

### Suggested Technical Corrigendum

Replace the first two bullets under 7.1.3p1 with:

  — All identifiers that begin with an underscore and either an uppercase letter
or another underscore are always reserved for any use<ins>, except those
identifiers which are lexically identical to keywords</ins>.
<ins><sup>footnote)</sup></ins>  
  — All identifiers that begin with an underscore are always reserved for use as
identifiers with file scope in both the ordinary and tag name spaces<ins>,
except those identifiers which are lexically identical to keywords</ins>.

<ins><sup>footnote)</sup> Allows identifiers spelled with a leading underscore
followed by an uppercase letter that match the spelling of a keyword to be used
as macro names.</ins>

---

Comment from WG14 on 2017-11-03:

Apr 2016 meeting

### Committee Discussion

> The committee accepts the first suggestion as the Proposed Technical
> Corrigendum.

### Proposed Technical Corrigendum

Change §7.1.3.p1 first bullet from:

>   — All identifiers that begin with an underscore and either an uppercase letter
> or another underscore are always reserved for any use.

to

>   — All identifiers that begin with an underscore and either an uppercase letter
> or another underscore are always reserved for any use, except those identifiers
> which are lexically identical to keywords. <sup>footnote)</sup>
>
> <sup>footnote)</sup> Allows identifiers spelled with a leading underscore
> followed by an uppercase letter that match the spelling of a keyword to be used
> as macro names by the program.
