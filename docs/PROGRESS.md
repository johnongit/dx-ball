# Reconstruction progress

Recover the authored functions as faithfully and exactly as possible first.
Then rebuild with the original Visual C++ 4.0 compiler and validate the full game behavior.
The current records cover gameplay, all five screen modes, resources, graphics and audio.

| Fact | Count |
| --- | ---: |
| Classified authored functions with source | 270 |
| Classified authored byte-exact functions | 250 |
| Classified authored functions awaiting exact matches | 20 |
| Provisional function candidates | 553 |
| Parent-owned compiler fragments, counted separately | 24 |
| Source-present functions | 475 |
| Functions with scoped semantic acceptance | 249 |
| Byte-exact functions | 395 |
| Complete exact code bytes | 85106 |
| Entries identified as runtime dependencies | 261 |
| Entries identified as compiler-generated code | 21 |
| Origin still unclassified | 1 |

The inventory includes game routines, runtime dependencies and compiler-generated code.
The authored inventory remains provisional. Historical Wine campaigns provide bounded
observations; full behavior of the restored VC4 game remains unverified.

Continue with the [remaining authored matches](research/exact/REMAINING_EXACT_FUNCTIONS.md#authored-candidates).
See [the architecture](ARCHITECTURE.md), [compiler matching](MATCHING.md),
and [historical play observations](research/ORIGINAL_CAMPAIGN.md).

Generated from the ledgers by `scripts/repo-python scripts/progress.py`.

October 18 source recovery: [three raster arithmetic corrections](research/exact/RASTER_WORD_ARITHMETIC.md),
ten focused original/native boundary comparisons, and all nine raster exacts
preserved. Counts above do not increase; twenty authored functions remain nonexact.

Further October 18 recovery: [rotation displacement and text-width corrections](research/exact/WORD_WIDTH_BOUNDARIES.md)
pass nine original/native boundary cases while preserving ten exact functions
and all twelve compared code identities. The authored exact count remains 250.

October 19: [genuine Kernel32 clock imports](research/exact/KERNEL_CLOCK_IMPORT.md)
restore the Windows boundary and native sample ownership. All 13 affected exacts
survive and 12 focused clock/transport cases pass. No function-count gain is
claimed; the paddle candidate changes from 677 bytes/68 differences to 679/496.
