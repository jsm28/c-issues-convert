### Summary

> The description for `nexttoward()` in Annex F should be changed to reference
> `nextafter` to be consistent with 7.12.11.4. and F.9.8.3.

### Details

> Currently, F.9.8.4 has: No additional requirements. From that, one could
> conclude that there is no required underflow or overflow for `nexttoward` by
> annex F. But, F.9.8.3 has two explicit error conditions on `nextafter` and
> 7.12.11.4 says `nexttoward` is similar to `nextafter`. We need to make it clear
> that `nextafter` and `nexttoward` have the same requirements with respect to
> range errors in annex F.

### Suggested Technical Corrigendum

In F.9.8.4 `nexttoward` change:

> No additional requirements.

to

> No additional requirements beyond `nextafter`.
