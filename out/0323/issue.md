**Summary:** The imaginary macro is missing in the normative text.

I think there may be a problem here with C99 (as amended by TC2). As far as I
can see there is no longer any mention of the imaginary macro in normative text,
which means implementations are not allowed to define it (because it is not
reserved for use by the implementation). Yet in Annex G it still recommends (in
informative text) that implementations which define `__STDC_IEC_559_COMPLEX__`
should define the imaginary macro. It also recommends that these implementations
should define `I` "to be `_Imaginary_I` (not `_Complex_I` as stated in 7.3)".
Yet implementations that do so would not comply with the normative text in 7.3
which requires I to be defined as `_Complex_I`.

Assuming that the intention was to allow implementations to follow the
recommendations in Annex G, but by an oversight the necessary normative text to
allow them to do so was omitted from TC2, perhaps in POSIX we should keep the
current text but mark some of it CX?

### Suggested Technical Corrigendum
