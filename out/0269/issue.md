**Problem** 7.18.1.1 reads:

> \[#1] The typedef name `int`*`N`*`_t` designates a signed integer type with
> width *N*, no padding bits, and a two's complement representation. Thus,
> `int8_t` denotes a signed integer type with a width of exactly 8 bits.
> 
> \[#2] The typedef name `uint`*`N`*`_t` designates an unsigned integer type with
> width *N*. Thus, `uint24_t` denotes an unsigned integer type with a width of
> exactly 24 bits.
> 
> \[#3] These types are optional. However, if an implementation provides integer
> types with widths of 8, 16, 32, or 64 bits, it shall define the corresponding
> typedef names.

The requirements for no padding bits and two's complement were added at a late
stage, and the implications to the text weren't fully thought through. In
particular:

* the second sentence of #1 is inconsistent with the first;
* the unsigned types should also have the "no padding bits" requirement (it can be derived from the requirement to provide both or neither of these types and the requirement that they have the same size, but it ought to be spelled out);
* the requirements in #3 aren't the same as those in #1, so an implementation can't have 8 bit types *with* padding bits or a sign-and-magnitude representation.

### Suggested Technical Corrigendum

Change this section to read:

> \[#1] The typedef name `int`*`N`*`_t` designates a signed integer type with
> width *N*, no padding bits, and a two's complement representation. Thus,
> `int8_t` denotes a signed integer type with a width of exactly 8 bits and those
> other properties.
> 
> \[#2] The typedef name `uint`*`N`*`_t` designates an unsigned integer type with
> width *N* and no padding bits. Thus, `uint24_t` denotes an unsigned integer type
> with a width of exactly 24 bits and no padding bits.
> 
> \[#3] These types are optional. However, if an implementation provides integer
> types with widths of 8, 16, 32, or 64 bits, no padding bits, and (for the signed
> types) that have a two's complement representation, it shall define the
> corresponding typedef names.

Or, alternatively:

> \[#3] These types are optional. However, if an implementation has a type with
> width 8, 16, 32, or 64 bits that meet the above requirements, it shall define
> the corresponding typedef names.
