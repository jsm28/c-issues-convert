Description: the current text requires that overflow handling is done before
rounding; this is counter intuitive, and not what is done for floating-point
overflow/rounding. As it happens, the order in which overflow and rounding are
done has no effect on the result when saturation is used for overflow handling.

Hence, if we change the order, the result remains the same for saturation.
However, with the current required order, mod\_wrap as overflow handling (which
is allowed but not required) cannot (reasonably) be implemented. It is therefore
proposed to change the order.

Proposed solution: change the required order of overflow handling and rounding.
