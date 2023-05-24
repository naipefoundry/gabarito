## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[5] Gabarito-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: i̅ ị̅ i̦̅ i̧̅ i̵̅ i̶̅ i̷̅ j̅ j̣̅ j̦̅ j̧̅ j̨̅ j̵̅ j̶̅ j̷̅ į̅ į̣̀ į̣́ į̣̂ į̣̃ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 670 among a set of 6 math glyphs.
The following math glyphs have a different width, though:

Width = 591:
plusminus, plus

Width = 467:
less, greater

Width = 545:
equal

Width = 571:
logicalnot

Width = 527:
multiply

Width = 575:
divide

Width = 535:
minus

Width = 559:
congruent, approxequal

Width = 544:
notequal

Width = 513:
greaterequal, lessequal

Width = 679:
uni2286, uni2289, uni2288, uni228A, uni2287

Width = 654:
uni228B
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* three (U+0033) contains a short segment B<<178.5,405.0>-<185.0,405.0>-<196.0,405.0>>

	* G (U+0047) contains a short segment B<<702.0,348.0>-<705.0,338.0>-<706.5,325.0>>

	* M (U+004D) contains a short segment L<<437.0,184.0>--<440.0,184.0>>

	* e (U+0065) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* m (U+006D) contains a short segment B<<475.0,328.0>-<476.0,319.0>-<476.0,309.5>>

	* m (U+006D) contains a short segment B<<476.0,309.5>-<476.0,300.0>-<476.0,291.0>>

	* yen (U+00A5) contains a short segment L<<210.0,262.0>--<210.0,262.0>>

	* yen (U+00A5) contains a short segment L<<310.0,262.0>--<310.0,262.0>>

	* registered (U+00AE) contains a short segment L<<334.0,436.0>--<331.0,436.0>>

	* ae (U+00E6) contains a short segment B<<327.0,281.0>-<327.0,282.0>-<327.0,283.0>>

	* egrave (U+00E8) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* eacute (U+00E9) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* ecircumflex (U+00EA) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* edieresis (U+00EB) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* emacron (U+0113) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* edotaccent (U+0117) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* eogonek (U+0119) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* ecaron (U+011B) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* Gbreve (U+011E) contains a short segment B<<702.0,348.0>-<705.0,338.0>-<706.5,325.0>>

	* Gdotaccent (U+0120) contains a short segment B<<702.0,348.0>-<705.0,338.0>-<706.5,325.0>>

	* uni0122 (U+0122) contains a short segment B<<702.0,348.0>-<705.0,338.0>-<706.5,325.0>>

	* Eng (U+014A) contains a short segment B<<503.0,-173.5>-<488.0,-169.0>-<483.0,-167.0>>

	* Eng (U+014A) contains a short segment B<<483.0,-83.0>-<488.0,-84.0>-<496.0,-86.0>>

	* Eng (U+014A) contains a short segment B<<496.0,-86.0>-<504.0,-88.0>-<514.0,-88.0>>

	* eng (U+014B) contains a short segment B<<320.0,-99.0>-<325.0,-100.0>-<333.0,-102.0>>

	* eng (U+014B) contains a short segment B<<333.0,-102.0>-<341.0,-104.0>-<351.0,-104.0>>

	* oe (U+0153) contains a short segment B<<873.0,243.0>-<873.0,236.0>-<872.5,228.0>>

	* oe (U+0153) contains a short segment B<<872.5,228.0>-<872.0,220.0>-<871.0,215.0>>

	* gamma (U+03B3) contains a short segment L<<158.0,45.0>--<158.0,45.0>>

	* gamma (U+03B3) contains a short segment L<<158.0,45.0>--<158.0,45.0>>

	* uni1EBD (U+1EBD) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* trademark (U+2122) contains a short segment L<<567.0,459.0>--<569.0,459.0>>

	* uni2209 (U+2209) contains a short segment L<<308.0,10.0>--<303.0,10.0>>

	* uni2284 (U+2284) contains a short segment L<<308.0,10.0>--<303.0,10.0>> 

	* uni2285 (U+2285) contains a short segment L<<362.0,498.0>--<367.0,498.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<103.0,217.0>--<91.0,372.0>> -> L<<91.0,372.0>--<81.0,709.0>>

	* exclam (U+0021): L<<209.0,709.0>--<199.0,373.0>> -> L<<199.0,373.0>--<187.0,217.0>>

	* exclamdown (U+00A1): L<<188.0,316.0>--<200.0,161.0>> -> L<<200.0,161.0>--<210.0,-176.0>>

	* exclamdown (U+00A1): L<<82.0,-176.0>--<92.0,160.0>> -> L<<92.0,160.0>--<104.0,316.0>>

	* gamma (U+03B3): L<<158.0,45.0>--<158.0,45.0>> -> L<<158.0,45.0>--<158.0,45.0>>

	* registered (U+00AE): L<<334.0,436.0>--<331.0,436.0>> -> L<<331.0,436.0>--<301.0,436.0>>

	* trademark (U+2122): L<<459.0,542.0>--<453.0,464.0>> -> L<<453.0,464.0>--<429.0,310.0>>

	* trademark (U+2122): L<<707.0,310.0>--<683.0,464.0>> -> L<<683.0,464.0>--<677.0,542.0>>

	* uni216F (U+216F): L<<273.0,509.0>--<247.0,382.0>> -> L<<247.0,382.0>--<198.0,96.0>>

	* uni216F (U+216F): L<<767.0,96.0>--<718.0,382.0>> -> L<<718.0,382.0>--<692.0,509.0>>

	* uni2209 (U+2209): L<<619.0,10.0>--<308.0,10.0>> -> L<<308.0,10.0>--<303.0,10.0>>

	* uni2284 (U+2284): L<<619.0,10.0>--<308.0,10.0>> -> L<<308.0,10.0>--<303.0,10.0>> 

	* uni2285 (U+2285): L<<51.0,498.0>--<362.0,498.0>> -> L<<362.0,498.0>--<367.0,498.0>> [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[7] Gabarito-ExtraBold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: i̅ ị̅ i̦̅ i̧̅ i̵̅ i̶̅ i̷̅ j̅ j̣̅ j̦̅ j̧̅ j̨̅ j̵̅ j̶̅ j̷̅ į̅ į̣̀ į̣́ į̣̂ į̣̃ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 620 among a set of 6 math glyphs.
The following math glyphs have a different width, though:

Width = 541:
plusminus, plus

Width = 513:
less, greater

Width = 535:
equal, notequal

Width = 559:
logicalnot

Width = 560:
multiply

Width = 566:
divide

Width = 429:
minus

Width = 598:
congruent

Width = 605:
approxequal

Width = 527:
greaterequal, lessequal

Width = 629:
uni2286, uni2289, uni2288, uni228A, uni2287

Width = 624:
uni228B
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* ampersand (U+0026): X=372.0,Y=-1.5 (should be at baseline 0?)

	* ampersand (U+0026): X=419.5,Y=682.5 (should be at cap-height 681?)

	* a (U+0061): X=151.5,Y=488.5 (should be at x-height 490?)

	* a (U+0061): X=271.0,Y=-1.5 (should be at baseline 0?)

	* g (U+0067): X=159.0,Y=1.0 (should be at baseline 0?)

	* h (U+0068): X=280.0,Y=489.5 (should be at x-height 490?)

	* j (U+006A): X=57.0,Y=2.0 (should be at baseline 0?)

	* l (U+006C): X=258.0,Y=-1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=264.0,Y=1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=307.0,Y=1.0 (should be at baseline 0?)

	* braceright (U+007D): X=28.0,Y=1.0 (should be at baseline 0?)

	* braceright (U+007D): X=70.0,Y=1.0 (should be at baseline 0?)

	* ordfeminine (U+00AA): X=112.5,Y=681.5 (should be at cap-height 681?)

	* plusminus (U+00B1): X=24.0,Y=-2.0 (should be at baseline 0?)

	* plusminus (U+00B1): X=517.0,Y=-2.0 (should be at baseline 0?)

	* agrave (U+00E0): X=271.0,Y=-1.5 (should be at baseline 0?)

	* aacute (U+00E1): X=271.0,Y=-1.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=271.0,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=271.0,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=462.0,Y=679.0 (should be at cap-height 681?)

	* adieresis (U+00E4): X=271.0,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=271.0,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=143.0,Y=679.0 (should be at cap-height 681?)

	* aring (U+00E5): X=388.0,Y=679.0 (should be at cap-height 681?)

	* aring (U+00E5): X=297.0,Y=680.0 (should be at cap-height 681?)

	* aring (U+00E5): X=234.0,Y=680.0 (should be at cap-height 681?)

	* ntilde (U+00F1): X=477.0,Y=679.0 (should be at cap-height 681?)

	* otilde (U+00F5): X=476.0,Y=679.0 (should be at cap-height 681?)

	* amacron (U+0101): X=271.0,Y=-1.5 (should be at baseline 0?)

	* abreve (U+0103): X=271.0,Y=-1.5 (should be at baseline 0?)

	* aogonek (U+0105): X=271.0,Y=-1.5 (should be at baseline 0?)

	* gbreve (U+011F): X=159.0,Y=1.0 (should be at baseline 0?)

	* gdotaccent (U+0121): X=159.0,Y=1.0 (should be at baseline 0?)

	* uni0123 (U+0123): X=159.0,Y=1.0 (should be at baseline 0?)

	* ij (U+0133): X=319.0,Y=2.0 (should be at baseline 0?)

	* lacute (U+013A): X=258.0,Y=-1.0 (should be at baseline 0?)

	* uni013C (U+013C): X=258.0,Y=-1.0 (should be at baseline 0?)

	* lcaron (U+013E): X=258.0,Y=-1.0 (should be at baseline 0?)

	* lslash (U+0142): X=300.0,Y=-1.0 (should be at baseline 0?)

	* eng (U+014B): X=350.0,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=152.0,Y=679.0 (should be at cap-height 681?)

	* uring (U+016F): X=397.0,Y=679.0 (should be at cap-height 681?)

	* uring (U+016F): X=306.0,Y=680.0 (should be at cap-height 681?)

	* uring (U+016F): X=243.0,Y=680.0 (should be at cap-height 681?)

	* uni01CE (U+01CE): X=271.0,Y=-1.5 (should be at baseline 0?)

	* uni0237 (U+0237): X=57.0,Y=2.0 (should be at baseline 0?)

	* ring (U+02DA): X=162.0,Y=679.0 (should be at cap-height 681?)

	* ring (U+02DA): X=407.0,Y=679.0 (should be at cap-height 681?)

	* ring (U+02DA): X=316.0,Y=680.0 (should be at cap-height 681?)

	* ring (U+02DA): X=253.0,Y=680.0 (should be at cap-height 681?)

	* tilde (U+02DC): X=481.0,Y=679.0 (should be at cap-height 681?)

	* tildecomb (U+0303): X=481.0,Y=679.0 (should be at cap-height 681?)

	* uni030A (U+030A): X=162.0,Y=679.0 (should be at cap-height 681?)

	* uni030A (U+030A): X=407.0,Y=679.0 (should be at cap-height 681?)

	* uni030A (U+030A): X=316.0,Y=680.0 (should be at cap-height 681?)

	* uni030A (U+030A): X=253.0,Y=680.0 (should be at cap-height 681?)

	* uni0394 (U+0394): X=204.0,Y=-1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=623.0,Y=1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=489.0,Y=-1.0 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=463.0,Y=679.0 (should be at cap-height 681?)

	* quoteright (U+2019): X=67.5,Y=683.0 (should be at cap-height 681?)

	* quotedblright (U+201D): X=67.5,Y=683.0 (should be at cap-height 681?)

	* quotedblright (U+201D): X=324.5,Y=683.0 (should be at cap-height 681?)

	* uni2077 (U+2077): X=343.0,Y=679.0 (should be at cap-height 681?)

	* uni2088 (U+2088): X=19.0,Y=1.0 (should be at baseline 0?)

	* uni2088 (U+2088): X=348.0,Y=1.0 (should be at baseline 0?)

	* uni21C5 (U+21C5): X=676.0,Y=-262.0 (should be at descender -260?)

	* uni2206 (U+2206): X=204.0,Y=-1.0 (should be at baseline 0?)

	* logicalor (U+2228): X=272.0,Y=-2.0 (should be at baseline 0?)

	* logicalor (U+2228): X=380.0,Y=-2.0 (should be at baseline 0?)

	* integral (U+222B): X=369.0,Y=682.0 (should be at cap-height 681?)

	* integral (U+222B): X=281.0,Y=682.0 (should be at cap-height 681?)

	* congruent (U+2245): X=193.0,Y=682.0 (should be at cap-height 681?)

	* lessequal (U+2264): X=442.0,Y=683.0 (should be at cap-height 681?)

	* greaterequal (U+2265): X=86.0,Y=683.0 (should be at cap-height 681?) 

	* fl (U+FB02): X=608.0,Y=-1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment B<<598.0,351.0>-<595.0,338.0>-<592.5,323.0>>

	* at (U+0040) contains a short segment B<<592.5,323.0>-<590.0,308.0>-<590.0,296.0>>

	* yen (U+00A5) contains a short segment L<<375.0,240.0>--<375.0,239.0>>

	* uni00B5 (U+00B5) contains a short segment B<<217.0,-13.0>-<211.0,-13.0>-<205.0,-13.0>>

	* Eng (U+014A) contains a short segment B<<433.5,-209.0>-<416.0,-205.0>-<411.0,-203.0>>

	* Eng (U+014A) contains a short segment B<<411.0,-64.0>-<417.0,-65.0>-<424.0,-66.0>>

	* Eng (U+014A) contains a short segment B<<424.0,-66.0>-<431.0,-67.0>-<444.0,-67.0>>

	* eng (U+014B) contains a short segment B<<281.0,-46.0>-<287.0,-48.0>-<293.5,-49.0>>

	* uni0394 (U+0394) contains a short segment L<<205.0,0.0>--<204.0,-1.0>>

	* uni0394 (U+0394) contains a short segment L<<204.0,-1.0>--<204.0,0.0>>

	* uni03BC (U+03BC) contains a short segment B<<217.0,-13.0>-<211.0,-13.0>-<205.0,-13.0>>

	* Euro (U+20AC) contains a short segment B<<250.0,325.0>-<250.0,316.0>-<250.0,309.0>>

	* Euro (U+20AC) contains a short segment B<<83.0,309.0>-<83.0,316.0>-<83.0,325.0>>

	* Euro (U+20AC) contains a short segment B<<83.0,325.0>-<83.0,332.0>-<83.0,340.0>>

	* Euro (U+20AC) contains a short segment B<<250.0,340.0>-<250.0,333.0>-<250.0,325.0>>

	* trademark (U+2122) contains a short segment L<<610.0,505.0>--<612.0,505.0>>

	* uni2206 (U+2206) contains a short segment L<<205.0,0.0>--<204.0,-1.0>>

	* uni2206 (U+2206) contains a short segment L<<204.0,-1.0>--<204.0,0.0>>

	* radical (U+221A) contains a short segment L<<570.0,854.0>--<572.0,854.0>>

	* lozenge (U+25CA) contains a short segment L<<19.0,334.0>--<19.0,345.0>> 

	* lozenge (U+25CA) contains a short segment L<<587.0,345.0>--<587.0,334.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<231.0,715.0>--<222.0,391.0>> -> L<<222.0,391.0>--<209.0,226.0>>

	* exclam (U+0021): L<<73.0,226.0>--<61.0,391.0>> -> L<<61.0,391.0>--<51.0,715.0>>

	* exclamdown (U+00A1): L<<210.0,298.0>--<223.0,132.0>> -> L<<223.0,132.0>--<232.0,-191.0>>

	* exclamdown (U+00A1): L<<52.0,-191.0>--<62.0,133.0>> -> L<<62.0,133.0>--<74.0,298.0>>

	* m (U+006D): L<<505.0,302.0>--<505.0,301.0>> -> L<<505.0,301.0>--<505.0,0.0>>

	* trademark (U+2122): L<<510.0,494.0>--<505.0,418.0>> -> L<<505.0,418.0>--<491.0,287.0>>

	* trademark (U+2122): L<<731.0,287.0>--<717.0,418.0>> -> L<<717.0,418.0>--<713.0,494.0>>

	* uni216F (U+216F): L<<283.0,395.0>--<274.0,324.0>> -> L<<274.0,324.0>--<246.0,157.0>>

	* uni216F (U+216F): L<<690.0,157.0>--<663.0,325.0>> -> L<<663.0,325.0>--<654.0,396.0>> 

	* yen (U+00A5): L<<375.0,240.0>--<375.0,239.0>> -> L<<375.0,239.0>--<375.0,204.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni03A9 (U+03A9): L<<334.0,142.0>--<335.0,0.0>>

	* uni03A9 (U+03A9): L<<416.0,0.0>--<417.0,142.0>>

	* uni2126 (U+2126): L<<334.0,142.0>--<335.0,0.0>> 

	* uni2126 (U+2126): L<<416.0,0.0>--<417.0,142.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] Gabarito-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: i̅ ị̅ i̦̅ i̧̅ i̵̅ i̶̅ i̷̅ j̅ j̣̅ j̦̅ j̧̅ j̨̅ j̵̅ j̶̅ j̷̅ į̅ į̣̀ į̣́ į̣̂ į̣̃ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 639 among a set of 6 math glyphs.
The following math glyphs have a different width, though:

Width = 560:
plusminus, plus

Width = 496:
less, greater

Width = 539:
equal, notequal

Width = 564:
logicalnot

Width = 548:
multiply

Width = 570:
divide

Width = 469:
minus

Width = 584:
congruent

Width = 588:
approxequal

Width = 522:
greaterequal, lessequal

Width = 648:
uni2286, uni2289, uni2288, uni228A, uni2287

Width = 636:
uni228B
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* ampersand (U+0026): X=372.0,Y=-1.0 (should be at baseline 0?)

	* ampersand (U+0026): X=417.0,Y=682.0 (should be at cap-height 681?)

	* a (U+0061): X=155.5,Y=488.0 (should be at x-height 489?)

	* l (U+006C): X=241.0,Y=1.0 (should be at baseline 0?)

	* section (U+00A7): X=33.0,Y=2.0 (should be at baseline 0?)

	* section (U+00A7): X=208.5,Y=0.5 (should be at baseline 0?)

	* uni00B2 (U+00B2): X=179.0,Y=679.0 (should be at cap-height 681?)

	* uni00B3 (U+00B3): X=164.0,Y=680.0 (should be at cap-height 681?)

	* onequarter (U+00BC): X=110.0,Y=-2.0 (should be at baseline 0?)

	* onehalf (U+00BD): X=110.0,Y=-2.0 (should be at baseline 0?)

	* threequarters (U+00BE): X=198.0,Y=-2.0 (should be at baseline 0?)

	* Oslash (U+00D8): X=284.0,Y=-2.0 (should be at baseline 0?)

	* atilde (U+00E3): X=290.5,Y=680.5 (should be at cap-height 681?)

	* ntilde (U+00F1): X=312.5,Y=680.5 (should be at cap-height 681?)

	* otilde (U+00F5): X=314.5,Y=680.5 (should be at cap-height 681?)

	* abreve (U+0103): X=218.5,Y=680.0 (should be at cap-height 681?)

	* abreve (U+0103): X=297.0,Y=680.0 (should be at cap-height 681?)

	* ccaron (U+010D): X=270.0,Y=679.0 (should be at cap-height 681?)

	* ecaron (U+011B): X=268.0,Y=679.0 (should be at cap-height 681?)

	* gbreve (U+011F): X=242.5,Y=680.0 (should be at cap-height 681?)

	* gbreve (U+011F): X=321.0,Y=680.0 (should be at cap-height 681?)

	* uni0122 (U+0122): X=371.0,Y=-259.5 (should be at descender -260?)

	* uni0136 (U+0136): X=327.0,Y=-259.5 (should be at descender -260?)

	* uni0137 (U+0137): X=279.0,Y=-259.5 (should be at descender -260?)

	* lacute (U+013A): X=241.0,Y=1.0 (should be at baseline 0?)

	* uni013B (U+013B): X=279.0,Y=-259.5 (should be at descender -260?)

	* uni013C (U+013C): X=241.0,Y=1.0 (should be at baseline 0?)

	* uni013C (U+013C): X=155.0,Y=-259.5 (should be at descender -260?)

	* lcaron (U+013E): X=241.0,Y=1.0 (should be at baseline 0?)

	* lslash (U+0142): X=268.0,Y=1.0 (should be at baseline 0?)

	* uni0145 (U+0145): X=366.0,Y=-259.5 (should be at descender -260?)

	* uni0146 (U+0146): X=283.0,Y=-259.5 (should be at descender -260?)

	* ncaron (U+0148): X=278.0,Y=679.0 (should be at cap-height 681?)

	* uni0156 (U+0156): X=312.0,Y=-259.5 (should be at descender -260?)

	* uni0157 (U+0157): X=126.0,Y=-259.5 (should be at descender -260?)

	* rcaron (U+0159): X=202.0,Y=679.0 (should be at cap-height 681?)

	* Scedilla (U+015E): X=240.0,Y=-2.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=320.0,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=227.0,Y=679.0 (should be at cap-height 681?)

	* ubreve (U+016D): X=235.5,Y=680.0 (should be at cap-height 681?)

	* ubreve (U+016D): X=314.0,Y=680.0 (should be at cap-height 681?)

	* zcaron (U+017E): X=239.0,Y=679.0 (should be at cap-height 681?)

	* uni01CE (U+01CE): X=256.0,Y=679.0 (should be at cap-height 681?)

	* uni0218 (U+0218): X=300.0,Y=-261.5 (should be at descender -260?)

	* uni0219 (U+0219): X=242.0,Y=-259.5 (should be at descender -260?)

	* uni021A (U+021A): X=286.0,Y=-259.5 (should be at descender -260?)

	* uni021B (U+021B): X=236.0,Y=-259.5 (should be at descender -260?)

	* caron (U+02C7): X=278.0,Y=679.0 (should be at cap-height 681?)

	* breve (U+02D8): X=239.5,Y=680.0 (should be at cap-height 681?)

	* breve (U+02D8): X=318.0,Y=680.0 (should be at cap-height 681?)

	* tilde (U+02DC): X=312.5,Y=680.5 (should be at cap-height 681?)

	* tildecomb (U+0303): X=312.5,Y=680.5 (should be at cap-height 681?)

	* uni0306 (U+0306): X=239.5,Y=680.0 (should be at cap-height 681?)

	* uni0306 (U+0306): X=318.0,Y=680.0 (should be at cap-height 681?)

	* uni030C (U+030C): X=278.0,Y=679.0 (should be at cap-height 681?)

	* uni0326 (U+0326): X=282.0,Y=-259.5 (should be at descender -260?)

	* alpha (U+03B1): X=613.0,Y=1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=488.0,Y=2.0 (should be at baseline 0?)

	* lambda (U+03BB): X=17.0,Y=-2.0 (should be at baseline 0?)

	* lambda (U+03BB): X=89.0,Y=679.0 (should be at cap-height 681?)

	* lambda (U+03BB): X=586.0,Y=2.0 (should be at baseline 0?)

	* lambda (U+03BB): X=162.0,Y=-2.0 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=302.5,Y=680.5 (should be at cap-height 681?)

	* quoteright (U+2019): X=187.5,Y=679.5 (should be at cap-height 681?)

	* quotedblright (U+201D): X=187.5,Y=679.5 (should be at cap-height 681?)

	* quotedblright (U+201D): X=422.5,Y=679.5 (should be at cap-height 681?)

	* fraction (U+2044): X=-135.0,Y=-2.0 (should be at baseline 0?)

	* uni2088 (U+2088): X=20.0,Y=-1.0 (should be at baseline 0?)

	* uni2088 (U+2088): X=338.0,Y=-2.0 (should be at baseline 0?)

	* emptyset (U+2205): X=116.0,Y=-2.0 (should be at baseline 0?) 

	* fl (U+FB02): X=582.0,Y=1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment B<<587.0,352.0>-<584.0,339.0>-<581.0,320.5>>

	* at (U+0040) contains a short segment B<<581.0,320.5>-<578.0,302.0>-<578.0,288.0>>

	* at (U+0040) contains a short segment B<<578.0,288.0>-<578.0,272.0>-<588.0,263.0>>

	* at (U+0040) contains a short segment B<<588.0,263.0>-<598.0,254.0>-<614.0,254.0>>

	* m (U+006D) contains a short segment B<<494.0,312.0>-<494.0,305.0>-<494.0,298.0>>

	* sterling (U+00A3) contains a short segment B<<282.0,242.0>-<283.0,237.0>-<283.0,232.0>>

	* sterling (U+00A3) contains a short segment B<<151.0,238.0>-<151.0,240.0>-<151.0,242.0>>

	* yen (U+00A5) contains a short segment L<<210.0,248.0>--<210.0,248.0>>

	* yen (U+00A5) contains a short segment L<<351.0,248.0>--<351.0,247.0>>

	* Eng (U+014A) contains a short segment B<<459.5,-196.0>-<443.0,-192.0>-<438.0,-189.0>>

	* Eng (U+014A) contains a short segment B<<438.0,-71.0>-<444.0,-72.0>-<451.5,-73.5>>

	* Eng (U+014A) contains a short segment B<<451.5,-73.5>-<459.0,-75.0>-<470.0,-75.0>>

	* eng (U+014B) contains a short segment B<<296.0,-66.0>-<301.0,-67.0>-<308.5,-68.5>>

	* uni0394 (U+0394) contains a short segment L<<167.0,0.0>--<167.0,0.0>>

	* uni0394 (U+0394) contains a short segment L<<167.0,0.0>--<167.0,0.0>>

	* Euro (U+20AC) contains a short segment B<<238.0,329.0>-<238.0,318.0>-<238.0,308.0>>

	* Euro (U+20AC) contains a short segment B<<96.0,308.0>-<95.0,318.0>-<96.0,329.0>>

	* Euro (U+20AC) contains a short segment B<<96.0,329.0>-<96.0,340.0>-<96.0,350.0>>

	* Euro (U+20AC) contains a short segment B<<238.0,350.0>-<237.0,340.0>-<238.0,329.0>>

	* trademark (U+2122) contains a short segment L<<594.0,488.0>--<596.0,488.0>>

	* uni2206 (U+2206) contains a short segment L<<167.0,0.0>--<167.0,0.0>>

	* uni2206 (U+2206) contains a short segment L<<167.0,0.0>--<167.0,0.0>>

	* radical (U+221A) contains a short segment L<<589.0,877.0>--<592.0,877.0>>

	* lozenge (U+25CA) contains a short segment L<<30.0,334.0>--<30.0,345.0>> 

	* lozenge (U+25CA) contains a short segment L<<573.0,345.0>--<573.0,334.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<223.0,713.0>--<214.0,384.0>> -> L<<214.0,384.0>--<201.0,223.0>>

	* exclam (U+0021): L<<85.0,223.0>--<73.0,384.0>> -> L<<73.0,384.0>--<63.0,713.0>>

	* exclamdown (U+00A1): L<<202.0,305.0>--<215.0,143.0>> -> L<<215.0,143.0>--<224.0,-185.0>>

	* exclamdown (U+00A1): L<<64.0,-185.0>--<73.0,143.0>> -> L<<73.0,143.0>--<86.0,305.0>>

	* trademark (U+2122): L<<491.0,514.0>--<486.0,435.0>> -> L<<486.0,435.0>--<468.0,296.0>>

	* trademark (U+2122): L<<722.0,296.0>--<704.0,435.0>> -> L<<704.0,435.0>--<699.0,514.0>>

	* uni0394 (U+0394): L<<167.0,0.0>--<167.0,0.0>> -> L<<167.0,0.0>--<167.0,0.0>>

	* uni216F (U+216F): L<<278.0,440.0>--<264.0,346.0>> -> L<<264.0,346.0>--<228.0,134.0>>

	* uni216F (U+216F): L<<719.0,134.0>--<684.0,347.0>> -> L<<684.0,347.0>--<669.0,440.0>>

	* uni2206 (U+2206): L<<167.0,0.0>--<167.0,0.0>> -> L<<167.0,0.0>--<167.0,0.0>> 

	* yen (U+00A5): L<<351.0,248.0>--<351.0,247.0>> -> L<<351.0,247.0>--<351.0,202.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* trademark (U+2122): B<<498.0,483.0>-<494.0,498.0>-<491.0,514.0>>/L<<491.0,514.0>--<486.0,435.0>> = 14.24113998027248 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni03A9 (U+03A9): L<<336.0,130.0>--<337.0,0.0>>

	* uni03A9 (U+03A9): L<<37.0,0.0>--<36.0,121.0>>

	* uni03A9 (U+03A9): L<<733.0,121.0>--<732.0,0.0>>

	* uni2126 (U+2126): L<<336.0,130.0>--<337.0,0.0>>

	* uni2126 (U+2126): L<<37.0,0.0>--<36.0,121.0>> 

	* uni2126 (U+2126): L<<733.0,121.0>--<732.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] Gabarito-Black.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: at	Contours detected: 4	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: at	Contours detected: 4	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: uni2783	Contours detected: 3	Expected: 4 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: i̅ ị̅ i̦̅ i̧̅ i̵̅ i̶̅ i̷̅ j̅ j̣̅ j̦̅ j̧̅ j̨̅ j̵̅ j̶̅ j̷̅ į̅ į̣̀ į̣́ į̣̂ į̣̃ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 608 among a set of 7 math glyphs.
The following math glyphs have a different width, though:

Width = 529:
plusminus, plus

Width = 524:
less, greater

Width = 533:
equal, notequal

Width = 556:
logicalnot

Width = 568:
multiply

Width = 564:
divide

Width = 402:
minus

Width = 617:
uni2286, uni2289, uni2288, approxequal, uni228A, uni228B, uni2287

Width = 531:
greaterequal, lessequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* percent (U+0025): X=538.0,Y=1.0 (should be at baseline 0?)

	* percent (U+0025): X=721.0,Y=1.0 (should be at baseline 0?)

	* ampersand (U+0026): X=422.0,Y=683.0 (should be at cap-height 681?)

	* period (U+002E): X=86.0,Y=2.0 (should be at baseline 0?)

	* period (U+002E): X=205.5,Y=2.0 (should be at baseline 0?)

	* colon (U+003A): X=86.0,Y=2.0 (should be at baseline 0?)

	* colon (U+003A): X=205.5,Y=2.0 (should be at baseline 0?)

	* Q (U+0051): X=472.0,Y=1.0 (should be at baseline 0?)

	* bracketleft (U+005B): X=221.0,Y=-1.0 (should be at baseline 0?)

	* bracketleft (U+005B): X=325.0,Y=-1.0 (should be at baseline 0?)

	* bracketright (U+005D): X=24.0,Y=-1.0 (should be at baseline 0?)

	* bracketright (U+005D): X=128.0,Y=-1.0 (should be at baseline 0?)

	* a (U+0061): X=149.5,Y=488.5 (should be at x-height 490?)

	* a (U+0061): X=265.5,Y=-1.5 (should be at baseline 0?)

	* h (U+0068): X=288.5,Y=492.0 (should be at x-height 490?)

	* cent (U+00A2): X=176.0,Y=683.0 (should be at cap-height 681?)

	* cent (U+00A2): X=343.0,Y=683.0 (should be at cap-height 681?)

	* section (U+00A7): X=303.0,Y=2.0 (should be at baseline 0?)

	* ordfeminine (U+00AA): X=107.5,Y=679.5 (should be at cap-height 681?)

	* Aring (U+00C5): X=227.0,Y=938.0 (should be at ascender 940?)

	* Aring (U+00C5): X=445.0,Y=938.0 (should be at ascender 940?)

	* agrave (U+00E0): X=265.5,Y=-1.5 (should be at baseline 0?)

	* aacute (U+00E1): X=265.5,Y=-1.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=265.5,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=265.5,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=472.0,Y=682.0 (should be at cap-height 681?)

	* adieresis (U+00E4): X=265.5,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=265.5,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=145.0,Y=683.0 (should be at cap-height 681?)

	* aring (U+00E5): X=397.0,Y=683.0 (should be at cap-height 681?)

	* ntilde (U+00F1): X=482.0,Y=682.0 (should be at cap-height 681?)

	* otilde (U+00F5): X=479.0,Y=682.0 (should be at cap-height 681?)

	* amacron (U+0101): X=265.5,Y=-1.5 (should be at baseline 0?)

	* abreve (U+0103): X=265.5,Y=-1.5 (should be at baseline 0?)

	* aogonek (U+0105): X=265.5,Y=-1.5 (should be at baseline 0?)

	* Cdotaccent (U+010A): X=360.0,Y=941.0 (should be at ascender 940?)

	* Edotaccent (U+0116): X=265.0,Y=941.0 (should be at ascender 940?)

	* Gdotaccent (U+0120): X=362.0,Y=941.0 (should be at ascender 940?)

	* Idotaccent (U+0130): X=132.0,Y=941.0 (should be at ascender 940?)

	* Uring (U+016E): X=218.0,Y=938.0 (should be at ascender 940?)

	* Uring (U+016E): X=436.0,Y=938.0 (should be at ascender 940?)

	* uring (U+016F): X=148.0,Y=683.0 (should be at cap-height 681?)

	* uring (U+016F): X=400.0,Y=683.0 (should be at cap-height 681?)

	* Zdotaccent (U+017B): X=305.0,Y=941.0 (should be at ascender 940?)

	* uni01CE (U+01CE): X=265.5,Y=-1.5 (should be at baseline 0?)

	* ring (U+02DA): X=162.0,Y=683.0 (should be at cap-height 681?)

	* ring (U+02DA): X=414.0,Y=683.0 (should be at cap-height 681?)

	* tilde (U+02DC): X=489.0,Y=682.0 (should be at cap-height 681?)

	* tildecomb (U+0303): X=489.0,Y=682.0 (should be at cap-height 681?)

	* uni030A (U+030A): X=162.0,Y=683.0 (should be at cap-height 681?)

	* uni030A (U+030A): X=414.0,Y=683.0 (should be at cap-height 681?)

	* uni0394 (U+0394): X=229.0,Y=-1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=629.0,Y=2.0 (should be at baseline 0?)

	* alpha (U+03B1): X=343.0,Y=0.5 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=465.0,Y=682.0 (should be at cap-height 681?)

	* quotesinglbase (U+201A): X=85.0,Y=-1.5 (should be at baseline 0?)

	* quotedblbase (U+201E): X=85.0,Y=-0.5 (should be at baseline 0?)

	* quotedblbase (U+201E): X=357.0,Y=-0.5 (should be at baseline 0?)

	* ellipsis (U+2026): X=86.0,Y=2.0 (should be at baseline 0?)

	* ellipsis (U+2026): X=205.5,Y=2.0 (should be at baseline 0?)

	* ellipsis (U+2026): X=377.0,Y=2.0 (should be at baseline 0?)

	* ellipsis (U+2026): X=496.5,Y=2.0 (should be at baseline 0?)

	* ellipsis (U+2026): X=671.0,Y=2.0 (should be at baseline 0?)

	* ellipsis (U+2026): X=790.5,Y=2.0 (should be at baseline 0?)

	* perthousand (U+2030): X=519.5,Y=1.0 (should be at baseline 0?)

	* perthousand (U+2030): X=703.0,Y=1.0 (should be at baseline 0?)

	* perthousand (U+2030): X=901.5,Y=1.0 (should be at baseline 0?)

	* perthousand (U+2030): X=1084.0,Y=1.0 (should be at baseline 0?)

	* uni2082 (U+2082): X=210.0,Y=-1.0 (should be at baseline 0?)

	* uni2082 (U+2082): X=339.0,Y=-1.0 (should be at baseline 0?)

	* uni2083 (U+2083): X=210.0,Y=-2.0 (should be at baseline 0?)

	* uni2089 (U+2089): X=216.0,Y=1.0 (should be at baseline 0?)

	* uni21C5 (U+21C5): X=681.0,Y=-258.0 (should be at descender -260?)

	* emptyset (U+2205): X=295.5,Y=2.0 (should be at baseline 0?)

	* uni2206 (U+2206): X=229.0,Y=-1.0 (should be at baseline 0?)

	* integral (U+222B): X=344.0,Y=682.5 (should be at cap-height 681?)

	* uni25CF (U+25CF): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni25CF (U+25CF): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni278A (U+278A): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni278A (U+278A): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni278B (U+278B): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni278B (U+278B): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni278C (U+278C): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni278C (U+278C): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni278D (U+278D): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni278D (U+278D): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni278E (U+278E): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni278E (U+278E): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni278F (U+278F): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni278F (U+278F): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni2790 (U+2790): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni2790 (U+2790): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni2791 (U+2791): X=238.0,Y=-2.0 (should be at baseline 0?)

	* uni2791 (U+2791): X=508.5,Y=-2.0 (should be at baseline 0?)

	* uni2792 (U+2792): X=508.0,Y=-2.0 (should be at baseline 0?)

	* uni2792 (U+2792): X=237.5,Y=-2.0 (should be at baseline 0?)

	* u1F10C (U+1F10C): X=238.0,Y=-2.0 (should be at baseline 0?) 

	* u1F10C (U+1F10C): X=508.5,Y=-2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* y (U+0079) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* y (U+0079) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* yen (U+00A5) contains a short segment L<<391.0,234.0>--<391.0,233.0>>

	* eth (U+00F0) contains a short segment L<<112.0,711.0>--<127.0,708.0>>

	* yacute (U+00FD) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* yacute (U+00FD) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* ydieresis (U+00FF) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* ydieresis (U+00FF) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* Eng (U+014A) contains a short segment B<<416.5,-218.0>-<398.0,-214.0>-<393.0,-212.0>>

	* Eng (U+014A) contains a short segment B<<393.0,-59.0>-<399.0,-60.0>-<406.0,-61.0>>

	* Eng (U+014A) contains a short segment B<<406.0,-61.0>-<413.0,-62.0>-<426.0,-62.0>>

	* eng (U+014B) contains a short segment B<<271.0,-33.0>-<277.0,-34.0>-<283.5,-35.0>>

	* ycircumflex (U+0177) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* ycircumflex (U+0177) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* uni0394 (U+0394) contains a short segment L<<230.0,0.0>--<229.0,-1.0>>

	* uni0394 (U+0394) contains a short segment L<<229.0,-1.0>--<229.0,0.0>>

	* ygrave (U+1EF3) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* ygrave (U+1EF3) contains a short segment L<<384.0,18.0>--<384.0,18.0>>

	* Euro (U+20AC) contains a short segment B<<258.0,322.0>-<258.0,316.0>-<258.0,310.0>>

	* Euro (U+20AC) contains a short segment B<<74.0,310.0>-<74.0,316.0>-<74.0,322.0>>

	* Euro (U+20AC) contains a short segment B<<74.0,322.0>-<74.0,328.0>-<74.0,333.0>>

	* Euro (U+20AC) contains a short segment B<<258.0,333.0>-<258.0,328.0>-<258.0,322.0>>

	* trademark (U+2122) contains a short segment L<<621.0,517.0>--<623.0,517.0>>

	* trademark (U+2122) contains a short segment B<<716.5,452.0>-<714.0,440.0>-<713.0,437.0>>

	* uni216F (U+216F) contains a short segment B<<644.0,365.0>-<639.0,350.0>-<634.5,337.5>>

	* uni216F (U+216F) contains a short segment B<<634.5,337.5>-<630.0,325.0>-<628.0,320.0>>

	* uni216F (U+216F) contains a short segment B<<301.0,319.0>-<299.0,325.0>-<295.0,337.0>>

	* uni216F (U+216F) contains a short segment B<<295.0,337.0>-<291.0,349.0>-<286.0,364.0>>

	* uni2206 (U+2206) contains a short segment L<<230.0,0.0>--<229.0,-1.0>>

	* uni2206 (U+2206) contains a short segment L<<229.0,-1.0>--<229.0,0.0>>

	* radical (U+221A) contains a short segment L<<521.0,726.0>--<521.0,726.0>>

	* lozenge (U+25CA) contains a short segment L<<12.0,334.0>--<12.0,345.0>> 

	* lozenge (U+25CA) contains a short segment L<<597.0,345.0>--<597.0,334.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<237.0,716.0>--<228.0,395.0>> -> L<<228.0,395.0>--<215.0,228.0>>

	* exclam (U+0021): L<<66.0,228.0>--<54.0,396.0>> -> L<<54.0,396.0>--<44.0,716.0>>

	* exclamdown (U+00A1): L<<216.0,293.0>--<229.0,125.0>> -> L<<229.0,125.0>--<238.0,-195.0>>

	* exclamdown (U+00A1): L<<45.0,-195.0>--<54.0,126.0>> -> L<<54.0,126.0>--<67.0,293.0>>

	* trademark (U+2122): L<<522.0,480.0>--<518.0,406.0>> -> L<<518.0,406.0>--<507.0,281.0>>

	* trademark (U+2122): L<<737.0,281.0>--<725.0,406.0>> -> L<<725.0,406.0>--<721.0,479.0>>

	* uni216F (U+216F): L<<286.0,364.0>--<281.0,310.0>> -> L<<281.0,310.0>--<258.0,172.0>>

	* uni216F (U+216F): L<<671.0,172.0>--<649.0,311.0>> -> L<<649.0,311.0>--<644.0,365.0>>

	* y (U+0079): L<<384.0,18.0>--<384.0,18.0>> -> L<<384.0,18.0>--<384.0,18.0>>

	* yacute (U+00FD): L<<384.0,18.0>--<384.0,18.0>> -> L<<384.0,18.0>--<384.0,18.0>>

	* ycircumflex (U+0177): L<<384.0,18.0>--<384.0,18.0>> -> L<<384.0,18.0>--<384.0,18.0>>

	* ydieresis (U+00FF): L<<384.0,18.0>--<384.0,18.0>> -> L<<384.0,18.0>--<384.0,18.0>>

	* yen (U+00A5): L<<391.0,234.0>--<391.0,233.0>> -> L<<391.0,233.0>--<391.0,205.0>> 

	* ygrave (U+1EF3): L<<384.0,18.0>--<384.0,18.0>> -> L<<384.0,18.0>--<384.0,18.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* trademark (U+2122): L<<725.0,406.0>--<721.0,479.0>>/B<<721.0,479.0>-<719.0,464.0>-<716.5,452.0>> = 10.731001736924052 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni03A9 (U+03A9): L<<333.0,150.0>--<334.0,0.0>>

	* uni03A9 (U+03A9): L<<405.0,0.0>--<406.0,150.0>>

	* uni2126 (U+2126): L<<333.0,150.0>--<334.0,0.0>> 

	* uni2126 (U+2126): L<<405.0,0.0>--<406.0,150.0>> [code: found-semi-vertical]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 28 | 470 | 29 | 393 | 0 |
| 0% | 0% | 3% | 51% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
