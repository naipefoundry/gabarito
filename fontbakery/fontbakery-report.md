## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[9] Gabarito-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "20" it should be 0 [code: bad-OS/2.sTypoLineGap]
* 🔥 **FAIL** hhea.lineGap is "20" it should be 0 [code: bad-hhea.lineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 324, but got 320 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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
plus, plusminus

Width = 467:
greater, less

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
approxequal, congruent

Width = 544:
notequal

Width = 513:
greaterequal, lessequal

Width = 679:
uni2288, uni2286, uni2289, uni228A

Width = 654:
uni228B, uni2287
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* ampersand (U+0026): X=371.0,Y=0.5 (should be at baseline 0?)

	* ampersand (U+0026): X=188.0,Y=680.5 (should be at cap-height 681?)

	* Q (U+0051): X=475.5,Y=1.0 (should be at baseline 0?)

	* S (U+0053): X=192.5,Y=1.0 (should be at baseline 0?)

	* a (U+0061): X=291.0,Y=-1.5 (should be at baseline 0?)

	* f (U+0066): X=305.0,Y=680.0 (should be at cap-height 681?)

	* r (U+0072): X=324.0,Y=489.0 (should be at x-height 488?)

	* t (U+0074): X=309.0,Y=1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=149.0,Y=-1.0 (should be at baseline 0?)

	* braceright (U+007D): X=163.0,Y=-1.0 (should be at baseline 0?)

	* uni00B3 (U+00B3): X=284.0,Y=683.0 (should be at cap-height 681?)

	* paragraph (U+00B6): X=195.5,Y=679.5 (should be at cap-height 681?)

	* threequarters (U+00BE): X=77.5,Y=681.5 (should be at cap-height 681?)

	* questiondown (U+00BF): X=442.0,Y=-2.0 (should be at baseline 0?)

	* agrave (U+00E0): X=291.0,Y=-1.5 (should be at baseline 0?)

	* aacute (U+00E1): X=291.0,Y=-1.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=291.0,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=291.0,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=110.0,Y=679.0 (should be at cap-height 681?)

	* adieresis (U+00E4): X=291.0,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=291.0,Y=-1.5 (should be at baseline 0?)

	* ntilde (U+00F1): X=144.0,Y=679.0 (should be at cap-height 681?)

	* otilde (U+00F5): X=151.0,Y=679.0 (should be at cap-height 681?)

	* amacron (U+0101): X=291.0,Y=-1.5 (should be at baseline 0?)

	* abreve (U+0103): X=291.0,Y=-1.5 (should be at baseline 0?)

	* aogonek (U+0105): X=291.0,Y=-1.5 (should be at baseline 0?)

	* Sacute (U+015A): X=192.5,Y=1.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=192.5,Y=1.0 (should be at baseline 0?)

	* Scaron (U+0160): X=192.5,Y=1.0 (should be at baseline 0?)

	* tcaron (U+0165): X=309.0,Y=1.0 (should be at baseline 0?)

	* tcaron (U+0165): X=340.0,Y=683.0 (should be at cap-height 681?)

	* uni01CE (U+01CE): X=291.0,Y=-1.5 (should be at baseline 0?)

	* uni0218 (U+0218): X=192.5,Y=1.0 (should be at baseline 0?)

	* uni021B (U+021B): X=309.0,Y=1.0 (should be at baseline 0?)

	* tilde (U+02DC): X=137.0,Y=679.0 (should be at cap-height 681?)

	* tildecomb (U+0303): X=137.0,Y=679.0 (should be at cap-height 681?)

	* alpha (U+03B1): X=597.0,Y=-1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=507.5,Y=-1.5 (should be at baseline 0?)

	* lambda (U+03BB): X=564.0,Y=-1.0 (should be at baseline 0?)

	* pi (U+03C0): X=604.0,Y=1.0 (should be at baseline 0?)

	* tau (U+03C4): X=306.0,Y=1.0 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=141.0,Y=679.0 (should be at cap-height 681?)

	* uni2076 (U+2076): X=131.5,Y=682.5 (should be at cap-height 681?)

	* uni2083 (U+2083): X=74.0,Y=-2.0 (should be at baseline 0?)

	* uni2088 (U+2088): X=230.0,Y=-2.0 (should be at baseline 0?)

	* uni2088 (U+2088): X=111.0,Y=-2.0 (should be at baseline 0?)

	* trademark (U+2122): X=26.0,Y=680.0 (should be at cap-height 681?)

	* trademark (U+2122): X=345.0,Y=680.0 (should be at cap-height 681?)

	* trademark (U+2122): X=405.0,Y=680.0 (should be at cap-height 681?)

	* trademark (U+2122): X=480.0,Y=680.0 (should be at cap-height 681?)

	* trademark (U+2122): X=656.0,Y=680.0 (should be at cap-height 681?)

	* trademark (U+2122): X=731.0,Y=680.0 (should be at cap-height 681?)

	* uni2196 (U+2196): X=749.0,Y=-2.0 (should be at baseline 0?)

	* partialdiff (U+2202): X=200.0,Y=683.0 (should be at cap-height 681?)

	* emptyset (U+2205): X=765.0,Y=683.0 (should be at cap-height 681?)

	* lozenge (U+25CA): X=240.0,Y=680.0 (should be at cap-height 681?)

	* lozenge (U+25CA): X=355.0,Y=680.0 (should be at cap-height 681?)

	* uni25CC (U+25CC): X=357.5,Y=1.5 (should be at baseline 0?)

	* uni25CC (U+25CC): X=406.5,Y=1.5 (should be at baseline 0?)

	* fi (U+FB01): X=305.0,Y=680.0 (should be at cap-height 681?) 

	* fl (U+FB02): X=305.0,Y=680.0 (should be at cap-height 681?) [code: found-misalignments]
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

	* eng (U+014B) contains a short segment B<<320.0,-83.0>-<325.0,-84.0>-<333.0,-86.0>>

	* oe (U+0153) contains a short segment B<<873.0,243.0>-<873.0,236.0>-<872.5,228.0>>

	* oe (U+0153) contains a short segment B<<872.5,228.0>-<872.0,220.0>-<871.0,215.0>>

	* gamma (U+03B3) contains a short segment L<<158.0,45.0>--<158.0,45.0>>

	* gamma (U+03B3) contains a short segment L<<158.0,45.0>--<158.0,45.0>>

	* uni1EBD (U+1EBD) contains a short segment B<<512.5,228.5>-<512.0,221.0>-<511.0,215.0>>

	* trademark (U+2122) contains a short segment L<<567.0,459.0>--<569.0,459.0>>

	* uni2209 (U+2209) contains a short segment L<<308.0,10.0>--<303.0,10.0>>

	* uni2284 (U+2284) contains a short segment L<<308.0,10.0>--<303.0,10.0>> 

	* uni2285 (U+2285) contains a short segment L<<362.0,508.0>--<367.0,508.0>> [code: found-short-segments]
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

	* uni2285 (U+2285): L<<51.0,508.0>--<362.0,508.0>> -> L<<362.0,508.0>--<367.0,508.0>> [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[10] Gabarito-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "20" it should be 0 [code: bad-OS/2.sTypoLineGap]
* 🔥 **FAIL** hhea.lineGap is "20" it should be 0 [code: bad-hhea.lineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 324, but got 320 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

Width = 585:
plus, plusminus

Width = 555:
greater, less

Width = 579:
equal

Width = 604:
logicalnot

Width = 605:
multiply

Width = 612:
divide

Width = 461:
minus

Width = 648:
congruent

Width = 656:
approxequal

Width = 578:
notequal

Width = 571:
greaterequal, lessequal

Width = 679:
uni2288, uni2286, uni2289, uni228A

Width = 674:
uni228B, uni2287
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* ampersand (U+0026): X=453.5,Y=737.5 (should be at cap-height 736?)

	* a (U+0061): X=163.5,Y=528.0 (should be at x-height 530?)

	* a (U+0061): X=292.5,Y=-1.5 (should be at baseline 0?)

	* h (U+0068): X=303.5,Y=529.5 (should be at x-height 530?)

	* l (U+006C): X=279.0,Y=-1.0 (should be at baseline 0?)

	* ordfeminine (U+00AA): X=121.0,Y=736.5 (should be at cap-height 736?)

	* onequarter (U+00BC): X=239.0,Y=737.0 (should be at cap-height 736?)

	* onequarter (U+00BC): X=136.0,Y=737.0 (should be at cap-height 736?)

	* onehalf (U+00BD): X=239.0,Y=737.0 (should be at cap-height 736?)

	* onehalf (U+00BD): X=136.0,Y=737.0 (should be at cap-height 736?)

	* agrave (U+00E0): X=292.5,Y=-1.5 (should be at baseline 0?)

	* aacute (U+00E1): X=292.5,Y=-1.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=292.5,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=292.5,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=499.0,Y=735.0 (should be at cap-height 736?)

	* adieresis (U+00E4): X=292.5,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=292.5,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=154.0,Y=734.0 (should be at cap-height 736?)

	* aring (U+00E5): X=419.0,Y=734.0 (should be at cap-height 736?)

	* aring (U+00E5): X=321.0,Y=735.0 (should be at cap-height 736?)

	* aring (U+00E5): X=252.0,Y=735.0 (should be at cap-height 736?)

	* ntilde (U+00F1): X=516.0,Y=735.0 (should be at cap-height 736?)

	* otilde (U+00F5): X=514.0,Y=735.0 (should be at cap-height 736?)

	* amacron (U+0101): X=292.5,Y=-1.5 (should be at baseline 0?)

	* abreve (U+0103): X=292.5,Y=-1.5 (should be at baseline 0?)

	* abreve (U+0103): X=287.0,Y=734.0 (should be at cap-height 736?)

	* aogonek (U+0105): X=292.5,Y=-1.5 (should be at baseline 0?)

	* gbreve (U+011F): X=302.0,Y=734.0 (should be at cap-height 736?)

	* uni0122 (U+0122): X=432.0,Y=-248.0 (should be at descender -250?)

	* uni0136 (U+0136): X=384.0,Y=-248.0 (should be at descender -250?)

	* uni0137 (U+0137): X=346.0,Y=-248.0 (should be at descender -250?)

	* lacute (U+013A): X=279.0,Y=-1.0 (should be at baseline 0?)

	* uni013B (U+013B): X=328.0,Y=-248.0 (should be at descender -250?)

	* uni013C (U+013C): X=279.0,Y=-1.0 (should be at baseline 0?)

	* uni013C (U+013C): X=211.0,Y=-248.0 (should be at descender -250?)

	* lcaron (U+013E): X=279.0,Y=-1.0 (should be at baseline 0?)

	* lslash (U+0142): X=325.0,Y=-1.0 (should be at baseline 0?)

	* uni0145 (U+0145): X=424.0,Y=-248.0 (should be at descender -250?)

	* uni0146 (U+0146): X=342.0,Y=-248.0 (should be at descender -250?)

	* uni0156 (U+0156): X=364.0,Y=-248.0 (should be at descender -250?)

	* uni0157 (U+0157): X=178.0,Y=-248.0 (should be at descender -250?)

	* ubreve (U+016D): X=296.0,Y=734.0 (should be at cap-height 736?)

	* uring (U+016F): X=164.0,Y=734.0 (should be at cap-height 736?)

	* uring (U+016F): X=429.0,Y=734.0 (should be at cap-height 736?)

	* uring (U+016F): X=331.0,Y=735.0 (should be at cap-height 736?)

	* uring (U+016F): X=262.0,Y=735.0 (should be at cap-height 736?)

	* uni01CE (U+01CE): X=292.5,Y=-1.5 (should be at baseline 0?)

	* uni0218 (U+0218): X=360.0,Y=-252.0 (should be at descender -250?)

	* uni0219 (U+0219): X=303.0,Y=-248.0 (should be at descender -250?)

	* uni021A (U+021A): X=351.0,Y=-248.0 (should be at descender -250?)

	* uni021B (U+021B): X=305.0,Y=-248.0 (should be at descender -250?)

	* breve (U+02D8): X=307.0,Y=734.0 (should be at cap-height 736?)

	* ring (U+02DA): X=175.0,Y=734.0 (should be at cap-height 736?)

	* ring (U+02DA): X=440.0,Y=734.0 (should be at cap-height 736?)

	* ring (U+02DA): X=342.0,Y=735.0 (should be at cap-height 736?)

	* ring (U+02DA): X=273.0,Y=735.0 (should be at cap-height 736?)

	* tilde (U+02DC): X=520.0,Y=735.0 (should be at cap-height 736?)

	* tildecomb (U+0303): X=520.0,Y=735.0 (should be at cap-height 736?)

	* uni0306 (U+0306): X=307.0,Y=734.0 (should be at cap-height 736?)

	* uni030A (U+030A): X=175.0,Y=734.0 (should be at cap-height 736?)

	* uni030A (U+030A): X=440.0,Y=734.0 (should be at cap-height 736?)

	* uni030A (U+030A): X=342.0,Y=735.0 (should be at cap-height 736?)

	* uni030A (U+030A): X=273.0,Y=735.0 (should be at cap-height 736?)

	* dotbelowcomb (U+0323): X=308.0,Y=-248.0 (should be at descender -250?)

	* uni0326 (U+0326): X=346.0,Y=-248.0 (should be at descender -250?)

	* uni0394 (U+0394): X=223.0,Y=-1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=674.0,Y=1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=529.0,Y=-1.5 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=500.0,Y=735.0 (should be at cap-height 736?)

	* quoteright (U+2019): X=73.5,Y=738.0 (should be at cap-height 736?)

	* quotedblright (U+201D): X=77.5,Y=738.0 (should be at cap-height 736?)

	* quotedblright (U+201D): X=356.5,Y=738.0 (should be at cap-height 736?)

	* uni2085 (U+2085): X=137.0,Y=2.0 (should be at baseline 0?)

	* logicalor (U+2228): X=293.0,Y=-2.0 (should be at baseline 0?)

	* logicalor (U+2228): X=411.0,Y=-2.0 (should be at baseline 0?)

	* uni2288 (U+2288): X=544.0,Y=735.0 (should be at cap-height 736?)

	* uni2289 (U+2289): X=438.0,Y=735.0 (should be at cap-height 736?) 

	* fl (U+FB02): X=658.0,Y=-1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment B<<646.0,380.0>-<644.0,365.0>-<641.5,349.0>>

	* at (U+0040) contains a short segment B<<641.5,349.0>-<639.0,333.0>-<639.0,321.0>>

	* yen (U+00A5) contains a short segment L<<407.0,259.0>--<407.0,259.0>>

	* uni00B5 (U+00B5) contains a short segment B<<235.0,-14.0>-<228.0,-14.0>-<222.0,-14.0>>

	* eth (U+00F0) contains a short segment L<<128.0,768.0>--<146.0,765.0>>

	* Eng (U+014A) contains a short segment B<<467.5,-227.5>-<448.0,-223.0>-<443.0,-221.0>>

	* Eng (U+014A) contains a short segment B<<443.0,-69.0>-<449.0,-70.0>-<457.0,-71.0>>

	* Eng (U+014A) contains a short segment B<<457.0,-71.0>-<465.0,-72.0>-<478.0,-72.0>>

	* eng (U+014B) contains a short segment B<<302.0,-69.0>-<309.0,-70.0>-<316.5,-71.0>>

	* uni0394 (U+0394) contains a short segment L<<223.0,0.0>--<223.0,-1.0>>

	* uni0394 (U+0394) contains a short segment L<<223.0,-1.0>--<222.0,0.0>>

	* uni03BC (U+03BC) contains a short segment B<<235.0,-14.0>-<228.0,-14.0>-<222.0,-14.0>>

	* Euro (U+20AC) contains a short segment B<<271.0,351.0>-<271.0,342.0>-<271.0,334.0>>

	* Euro (U+20AC) contains a short segment B<<89.0,334.0>-<89.0,342.0>-<89.0,351.0>>

	* Euro (U+20AC) contains a short segment B<<89.0,351.0>-<89.0,359.0>-<89.0,367.0>>

	* Euro (U+20AC) contains a short segment B<<271.0,367.0>-<271.0,359.0>-<271.0,351.0>>

	* trademark (U+2122) contains a short segment L<<661.0,547.0>--<663.0,547.0>>

	* uni216F (U+216F) contains a short segment B<<332.0,347.0>-<328.0,358.0>-<321.0,379.5>>

	* radical (U+221A) contains a short segment L<<615.0,922.0>--<617.0,922.0>>

	* lozenge (U+25CA) contains a short segment L<<20.0,361.0>--<20.0,373.0>> 

	* lozenge (U+25CA) contains a short segment L<<636.0,373.0>--<636.0,361.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<251.0,773.0>--<241.0,423.0>> -> L<<241.0,423.0>--<227.0,244.0>>

	* exclam (U+0021): L<<79.0,244.0>--<65.0,423.0>> -> L<<65.0,423.0>--<55.0,773.0>>

	* exclamdown (U+00A1): L<<228.0,322.0>--<242.0,143.0>> -> L<<242.0,143.0>--<252.0,-207.0>>

	* exclamdown (U+00A1): L<<56.0,-207.0>--<66.0,143.0>> -> L<<66.0,143.0>--<80.0,322.0>>

	* m (U+006D): L<<546.0,327.0>--<546.0,326.0>> -> L<<546.0,326.0>--<546.0,0.0>>

	* trademark (U+2122): L<<552.0,534.0>--<547.0,450.0>> -> L<<547.0,450.0>--<532.0,310.0>>

	* trademark (U+2122): L<<791.0,310.0>--<775.0,450.0>> -> L<<775.0,450.0>--<771.0,534.0>>

	* uni216F (U+216F): L<<306.0,426.0>--<297.0,349.0>> -> L<<297.0,349.0>--<267.0,170.0>> 

	* uni216F (U+216F): L<<745.0,170.0>--<716.0,350.0>> -> L<<716.0,350.0>--<706.0,426.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni03A9 (U+03A9): L<<30.0,0.0>--<29.0,151.0>>

	* uni03A9 (U+03A9): L<<361.0,154.0>--<362.0,0.0>>

	* uni03A9 (U+03A9): L<<449.0,0.0>--<450.0,154.0>> 

	* uni03A9 (U+03A9): L<<782.0,151.0>--<781.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] Gabarito-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "20" it should be 0 [code: bad-OS/2.sTypoLineGap]
* 🔥 **FAIL** hhea.lineGap is "20" it should be 0 [code: bad-hhea.lineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 324, but got 320 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

Width = 587:
plus, plusminus

Width = 522:
greater, less

Width = 566:
equal, notequal

Width = 592:
logicalnot

Width = 576:
multiply

Width = 598:
divide

Width = 489:
minus

Width = 615:
congruent

Width = 620:
approxequal

Width = 549:
greaterequal, lessequal

Width = 679:
uni2288, uni2286, uni2289, uni228A

Width = 667:
uni228B, uni2287
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment B<<617.0,370.0>-<614.0,356.0>-<611.5,337.0>>

	* at (U+0040) contains a short segment B<<611.5,337.0>-<609.0,318.0>-<609.0,304.0>>

	* at (U+0040) contains a short segment B<<609.0,304.0>-<609.0,287.0>-<619.0,278.0>>

	* at (U+0040) contains a short segment B<<619.0,278.0>-<629.0,269.0>-<645.0,269.0>>

	* m (U+006D) contains a short segment B<<520.0,327.0>-<520.0,321.0>-<520.0,313.0>>

	* sterling (U+00A3) contains a short segment B<<298.0,254.0>-<298.0,249.0>-<298.0,245.0>>

	* yen (U+00A5) contains a short segment L<<371.0,260.0>--<371.0,260.0>>

	* Eng (U+014A) contains a short segment B<<480.5,-207.0>-<463.0,-203.0>-<458.0,-200.0>>

	* Eng (U+014A) contains a short segment B<<458.0,-74.0>-<464.0,-75.0>-<472.0,-76.5>>

	* Eng (U+014A) contains a short segment B<<472.0,-76.5>-<480.0,-78.0>-<492.0,-78.0>>

	* eng (U+014B) contains a short segment B<<309.0,-74.0>-<315.0,-75.0>-<323.0,-76.5>>

	* uni0394 (U+0394) contains a short segment L<<179.0,0.0>--<179.0,0.0>>

	* uni0394 (U+0394) contains a short segment L<<179.0,0.0>--<178.0,0.0>>

	* Euro (U+20AC) contains a short segment B<<251.0,345.0>-<251.0,334.0>-<251.0,323.0>>

	* Euro (U+20AC) contains a short segment B<<100.0,323.0>-<100.0,334.0>-<99.0,345.0>>

	* Euro (U+20AC) contains a short segment B<<99.0,345.0>-<100.0,356.0>-<100.0,367.0>>

	* Euro (U+20AC) contains a short segment B<<251.0,367.0>-<251.0,356.0>-<251.0,345.0>>

	* trademark (U+2122) contains a short segment L<<626.0,514.0>--<628.0,514.0>> 

	* radical (U+221A) contains a short segment L<<617.0,920.0>--<621.0,920.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<235.0,749.0>--<225.0,404.0>> -> L<<225.0,404.0>--<212.0,234.0>>

	* exclam (U+0021): L<<88.0,234.0>--<75.0,404.0>> -> L<<75.0,404.0>--<65.0,749.0>>

	* exclamdown (U+00A1): L<<213.0,320.0>--<226.0,150.0>> -> L<<226.0,150.0>--<236.0,-195.0>>

	* exclamdown (U+00A1): L<<66.0,-195.0>--<76.0,150.0>> -> L<<76.0,150.0>--<89.0,320.0>>

	* trademark (U+2122): L<<517.0,539.0>--<512.0,456.0>> -> L<<512.0,456.0>--<494.0,310.0>>

	* trademark (U+2122): L<<760.0,310.0>--<741.0,456.0>> -> L<<741.0,456.0>--<736.0,539.0>>

	* uni0394 (U+0394): L<<179.0,0.0>--<178.0,0.0>> -> L<<178.0,0.0>--<9.0,0.0>>

	* uni216F (U+216F): L<<293.0,458.0>--<278.0,362.0>> -> L<<278.0,362.0>--<241.0,143.0>> 

	* uni216F (U+216F): L<<753.0,143.0>--<717.0,362.0>> -> L<<717.0,362.0>--<702.0,459.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni03A9 (U+03A9): L<<353.0,137.0>--<354.0,0.0>>

	* uni03A9 (U+03A9): L<<38.0,0.0>--<37.0,128.0>>

	* uni03A9 (U+03A9): L<<453.0,0.0>--<454.0,137.0>> 

	* uni03A9 (U+03A9): L<<770.0,128.0>--<769.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] Gabarito-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "20" it should be 0 [code: bad-OS/2.sTypoLineGap]
* 🔥 **FAIL** hhea.lineGap is "20" it should be 0 [code: bad-hhea.lineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 324, but got 320 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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


* ⚠ **WARN** The most common width is 670 among a set of 7 math glyphs.
The following math glyphs have a different width, though:

Width = 583:
plus, plusminus

Width = 577:
greater, less

Width = 587:
equal, notequal

Width = 612:
logicalnot

Width = 625:
multiply

Width = 621:
divide

Width = 443:
minus

Width = 680:
approxequal

Width = 585:
greaterequal, lessequal

Width = 679:
uni2289, uni228A, uni2286, uni2287, uni2288, uni228B
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** hhea lineGap is not equal to 0. [code: hhea]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* percent (U+0025): X=592.5,Y=1.5 (should be at baseline 0?)

	* percent (U+0025): X=794.0,Y=1.5 (should be at baseline 0?)

	* ampersand (U+0026): X=464.0,Y=752.0 (should be at cap-height 750?)

	* Q (U+0051): X=520.0,Y=1.0 (should be at baseline 0?)

	* bracketleft (U+005B): X=243.0,Y=-1.0 (should be at baseline 0?)

	* bracketleft (U+005B): X=358.0,Y=-1.0 (should be at baseline 0?)

	* bracketright (U+005D): X=26.0,Y=-1.0 (should be at baseline 0?)

	* bracketright (U+005D): X=141.0,Y=-1.0 (should be at baseline 0?)

	* a (U+0061): X=164.5,Y=538.0 (should be at x-height 540?)

	* a (U+0061): X=292.5,Y=-1.5 (should be at baseline 0?)

	* h (U+0068): X=317.5,Y=542.0 (should be at x-height 540?)

	* cent (U+00A2): X=194.0,Y=752.0 (should be at cap-height 750?)

	* cent (U+00A2): X=378.0,Y=752.0 (should be at cap-height 750?)

	* section (U+00A7): X=334.0,Y=2.0 (should be at baseline 0?)

	* ordfeminine (U+00AA): X=118.5,Y=748.5 (should be at cap-height 750?)

	* uni00B3 (U+00B3): X=17.0,Y=751.0 (should be at cap-height 750?)

	* cedilla (U+00B8): X=298.0,Y=-251.0 (should be at descender -250?)

	* cedilla (U+00B8): X=298.0,Y=-251.0 (should be at descender -250?)

	* onequarter (U+00BC): X=250.0,Y=749.0 (should be at cap-height 750?)

	* onequarter (U+00BC): X=136.0,Y=749.0 (should be at cap-height 750?)

	* onehalf (U+00BD): X=250.0,Y=749.0 (should be at cap-height 750?)

	* onehalf (U+00BD): X=136.0,Y=749.0 (should be at cap-height 750?)

	* Ccedilla (U+00C7): X=370.0,Y=-251.0 (should be at descender -250?)

	* Ccedilla (U+00C7): X=370.0,Y=-251.0 (should be at descender -250?)

	* agrave (U+00E0): X=292.5,Y=-1.5 (should be at baseline 0?)

	* aacute (U+00E1): X=292.5,Y=-1.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=292.5,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=292.5,Y=-1.5 (should be at baseline 0?)

	* atilde (U+00E3): X=519.0,Y=751.0 (should be at cap-height 750?)

	* adieresis (U+00E4): X=292.5,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=292.5,Y=-1.5 (should be at baseline 0?)

	* aring (U+00E5): X=159.0,Y=752.0 (should be at cap-height 750?)

	* aring (U+00E5): X=437.0,Y=752.0 (should be at cap-height 750?)

	* ccedilla (U+00E7): X=269.0,Y=-251.0 (should be at descender -250?)

	* ccedilla (U+00E7): X=269.0,Y=-251.0 (should be at descender -250?)

	* ntilde (U+00F1): X=531.0,Y=751.0 (should be at cap-height 750?)

	* otilde (U+00F5): X=527.0,Y=751.0 (should be at cap-height 750?)

	* amacron (U+0101): X=292.5,Y=-1.5 (should be at baseline 0?)

	* abreve (U+0103): X=292.5,Y=-1.5 (should be at baseline 0?)

	* aogonek (U+0105): X=292.5,Y=-1.5 (should be at baseline 0?)

	* uni0122 (U+0122): X=438.5,Y=-249.0 (should be at descender -250?)

	* uni0136 (U+0136): X=390.5,Y=-249.0 (should be at descender -250?)

	* uni0137 (U+0137): X=359.5,Y=-249.0 (should be at descender -250?)

	* uni013B (U+013B): X=329.5,Y=-249.0 (should be at descender -250?)

	* uni013C (U+013C): X=221.5,Y=-249.0 (should be at descender -250?)

	* uni0145 (U+0145): X=429.5,Y=-249.0 (should be at descender -250?)

	* uni0146 (U+0146): X=350.5,Y=-249.0 (should be at descender -250?)

	* uni0156 (U+0156): X=367.5,Y=-249.0 (should be at descender -250?)

	* uni0157 (U+0157): X=186.5,Y=-249.0 (should be at descender -250?)

	* Scedilla (U+015E): X=241.5,Y=-248.0 (should be at descender -250?)

	* scedilla (U+015F): X=245.0,Y=-251.0 (should be at descender -250?)

	* scedilla (U+015F): X=245.0,Y=-251.0 (should be at descender -250?)

	* uring (U+016F): X=163.0,Y=752.0 (should be at cap-height 750?)

	* uring (U+016F): X=441.0,Y=752.0 (should be at cap-height 750?)

	* uni01CE (U+01CE): X=292.5,Y=-1.5 (should be at baseline 0?)

	* uni0219 (U+0219): X=314.5,Y=-249.0 (should be at descender -250?)

	* uni021A (U+021A): X=362.5,Y=-249.0 (should be at descender -250?)

	* uni021B (U+021B): X=320.5,Y=-249.0 (should be at descender -250?)

	* ring (U+02DA): X=178.0,Y=752.0 (should be at cap-height 750?)

	* ring (U+02DA): X=456.0,Y=752.0 (should be at cap-height 750?)

	* tilde (U+02DC): X=538.0,Y=751.0 (should be at cap-height 750?)

	* tildecomb (U+0303): X=538.0,Y=751.0 (should be at cap-height 750?)

	* uni030A (U+030A): X=178.0,Y=752.0 (should be at cap-height 750?)

	* uni030A (U+030A): X=456.0,Y=752.0 (should be at cap-height 750?)

	* uni0326 (U+0326): X=357.5,Y=-249.0 (should be at descender -250?)

	* uni0327 (U+0327): X=298.0,Y=-251.0 (should be at descender -250?)

	* uni0327 (U+0327): X=298.0,Y=-251.0 (should be at descender -250?)

	* uni0394 (U+0394): X=252.0,Y=-1.0 (should be at baseline 0?)

	* alpha (U+03B1): X=693.0,Y=2.0 (should be at baseline 0?)

	* alpha (U+03B1): X=378.0,Y=1.0 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=512.0,Y=751.0 (should be at cap-height 750?)

	* perthousand (U+2030): X=572.5,Y=1.5 (should be at baseline 0?)

	* perthousand (U+2030): X=774.0,Y=1.5 (should be at baseline 0?)

	* perthousand (U+2030): X=992.5,Y=1.5 (should be at baseline 0?)

	* perthousand (U+2030): X=1194.0,Y=1.5 (should be at baseline 0?)

	* uni2083 (U+2083): X=147.0,Y=-1.5 (should be at baseline 0?)

	* integral (U+222B): X=378.5,Y=751.0 (should be at cap-height 750?)

	* uni278A (U+278A): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni278A (U+278A): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni278B (U+278B): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni278B (U+278B): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni278C (U+278C): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni278C (U+278C): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni278D (U+278D): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni278D (U+278D): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni278E (U+278E): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni278E (U+278E): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni278F (U+278F): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni278F (U+278F): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni2790 (U+2790): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni2790 (U+2790): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni2791 (U+2791): X=262.0,Y=-2.0 (should be at baseline 0?)

	* uni2791 (U+2791): X=560.0,Y=-2.0 (should be at baseline 0?)

	* uni2792 (U+2792): X=559.5,Y=-2.0 (should be at baseline 0?)

	* uni2792 (U+2792): X=262.0,Y=-2.0 (should be at baseline 0?)

	* u1F10C (U+1F10C): X=262.0,Y=-2.0 (should be at baseline 0?) 

	* u1F10C (U+1F10C): X=560.0,Y=-2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* eth (U+00F0) contains a short segment L<<123.0,783.0>--<140.0,780.0>>

	* Eng (U+014A) contains a short segment B<<458.5,-240.5>-<438.0,-236.0>-<433.0,-234.0>>

	* Eng (U+014A) contains a short segment B<<433.0,-65.0>-<440.0,-66.0>-<447.5,-67.0>>

	* Eng (U+014A) contains a short segment B<<447.5,-67.0>-<455.0,-68.0>-<469.0,-68.0>>

	* eng (U+014B) contains a short segment B<<298.0,-65.0>-<305.0,-66.0>-<312.5,-67.0>>

	* uni0394 (U+0394) contains a short segment L<<253.0,0.0>--<252.0,-1.0>>

	* uni0394 (U+0394) contains a short segment L<<252.0,-1.0>--<252.0,0.0>>

	* Euro (U+20AC) contains a short segment B<<284.0,355.0>-<284.0,348.0>-<284.0,341.0>>

	* Euro (U+20AC) contains a short segment B<<82.0,341.0>-<82.0,348.0>-<82.0,355.0>>

	* Euro (U+20AC) contains a short segment B<<82.0,355.0>-<82.0,361.0>-<82.0,367.0>>

	* Euro (U+20AC) contains a short segment B<<284.0,367.0>-<284.0,361.0>-<284.0,355.0>>

	* trademark (U+2122) contains a short segment L<<684.0,569.0>--<686.0,569.0>>

	* uni216F (U+216F) contains a short segment B<<709.0,403.0>-<703.0,385.0>-<698.5,371.5>>

	* uni216F (U+216F) contains a short segment B<<698.5,371.5>-<694.0,358.0>-<692.0,352.0>>

	* uni216F (U+216F) contains a short segment B<<332.0,351.0>-<330.0,357.0>-<325.5,371.0>>

	* uni216F (U+216F) contains a short segment B<<325.5,371.0>-<321.0,385.0>-<315.0,402.0>>

	* lozenge (U+25CA) contains a short segment L<<13.0,368.0>--<13.0,380.0>> 

	* lozenge (U+25CA) contains a short segment L<<658.0,380.0>--<658.0,368.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<261.0,789.0>--<251.0,435.0>> -> L<<251.0,435.0>--<237.0,251.0>>

	* exclam (U+0021): L<<73.0,251.0>--<59.0,436.0>> -> L<<59.0,436.0>--<49.0,789.0>>

	* exclamdown (U+00A1): L<<238.0,323.0>--<252.0,138.0>> -> L<<252.0,138.0>--<262.0,-215.0>>

	* exclamdown (U+00A1): L<<50.0,-215.0>--<60.0,139.0>> -> L<<60.0,139.0>--<74.0,323.0>>

	* radical (U+221A): L<<353.0,123.0>--<601.0,884.0>> -> L<<601.0,884.0>--<637.0,994.0>>

	* trademark (U+2122): L<<575.0,530.0>--<571.0,447.0>> -> L<<571.0,447.0>--<558.0,310.0>>

	* trademark (U+2122): L<<623.0,311.0>--<585.0,481.0>> -> L<<585.0,481.0>--<575.0,530.0>>

	* trademark (U+2122): L<<812.0,310.0>--<798.0,447.0>> -> L<<798.0,447.0>--<794.0,528.0>>

	* uni216F (U+216F): L<<315.0,402.0>--<309.0,341.0>> -> L<<309.0,341.0>--<284.0,189.0>> 

	* uni216F (U+216F): L<<740.0,189.0>--<715.0,342.0>> -> L<<715.0,342.0>--<709.0,403.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* trademark (U+2122): L<<585.0,481.0>--<575.0,530.0>>/L<<575.0,530.0>--<571.0,447.0>> = 14.293728312264973 

	* trademark (U+2122): L<<798.0,447.0>--<794.0,528.0>>/B<<794.0,528.0>-<791.0,512.0>-<788.5,498.5>> = 13.446779854316407 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni03A9 (U+03A9): L<<367.0,165.0>--<368.0,0.0>> 

	* uni03A9 (U+03A9): L<<446.0,0.0>--<447.0,165.0>> [code: found-semi-vertical]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 31 | 470 | 29 | 382 | 0 |
| 0% | 1% | 3% | 51% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
