### Summary

TS 18661-4 neglected to specify the preferred quantum exponent for its new
functions. This was an oversight. The following suggested TC adds the missing
specification.

### Suggested Technical Corrigendum

In TS 18661-4, at the end of clause 7, append:

In the Preferred Quantum Exponents table in 5.2.4.2.2a#7, insert before the
final row:

| ```c rsqrt ``` | −floor(Q(`x`)/2) |
| --- | --- |
| ```c compoundn ``` | floor(`n` × min(0, Q(`x`))) |
| ```c rootn ``` | floor(Q(`x`)/`n`) |
| ```c pown ``` | floor(`n` × Q(`x`)) |
| ```c powr ``` | floor(`y` × Q(`x`)) |

In TS 18661-4, at the end of clause 8, append:

In the Preferred Exponents Table in 5.2.4.2.2a#7, append:

| reduction functions | unspecified |
| --- | --- |
