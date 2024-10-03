Subject: Compatibility of complete and incomplete types.

The Committee has already endorsed the concept of using incomplete types which
are completed in some translation units and left incomplete in others for
encapsulation and data hiding (cf. [Defect Report #059](issue:0059)). However, I
can find nothing in the Standard which allows the incomplete type to be
compatible with the completed type, which causes such usage to be not strictly
conforming. I believe this to be an oversight.
