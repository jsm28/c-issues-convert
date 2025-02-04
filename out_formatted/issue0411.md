## Issue 0411: Predefined macro values

**This issue has been automatically converted from the original issue lists and some formatting may not have been preserved.**

Authors: Project Editor, Project Editor (Larry Jones)  
Date: 2012-01-18  
Submitted against: C11 / C17  
Status: Fixed  
Fixed in: C11 TC1  
Converted from: [n2396.htm](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2396.htm)

### Summary

The actual values for the predefined macros `__STDC_VERSION__` and
`__STDC_LIB_EXT1__` should be specified.

### Suggested Technical Corrigendum

Change the relevant list entry in 6.10.8.1 to:

> `__STDC_VERSION__` The integer constant `201112L`.

Change the relevant list entry in 6.10.8.3 to:

> `__STDC_LIB_EXT1__` The integer constant `201112L`.

---

Comment from WG14 on 2012-02-17:

Feb 2012 meeting

> ### Committee Discussion
>
> > * The committee asked the Convener to look into making this an errata if possible.
>
> ### Proposed Technical Corrigendum
>
> Change 6.10.8.1 from:
>
> > `__STDC_VERSION__` The integer constant`201ymmL`.<sup>178\)</sup>
>
> to:
>
> > `__STDC_VERSION__` The integer constant `201112L`.<sup>178\)</sup>
>
> Change 6.10.8.3 from:
>
> > `__STDC_LIB_EXT1__` The integer constant`201ymmL`, intended to indicate support
> > for the extensions defined in annex K (Bounds-checking
> > interfaces).<sup>179\)</sup>
>
> to:
>
> > `__STDC_LIB_EXT1__` The integer constant `201112L`, intended to indicate support
> > for the extensions defined in annex K (Bounds-checking
> > interfaces).<sup>179\)</sup>
