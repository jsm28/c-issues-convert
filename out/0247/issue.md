### Problem

I can see nothing that says or implies that production of an unspecified value
is a form of unspecified behaviour, and similarly for implementation-defined
values. It is therefore arguable that a program is strictly-conforming even if
its output depends on an unspecified value.

### Suggested Technical Corrigendum

Add a new paragraph 4#2a after 4#2:

> \[#2a] An evaluation that makes use of an unspecified or implementation-defined
> value is a form of unspecified or implementation-defined behaviour respectively.
