# Last-brick board-transition boundary

The October 18 resumed investigation establishes a limit on the last-brick
controller's caller contract. A level-skip bonus replaces the board during the
frame, but leaves `dxball_remaining_bricks` and the lightning deadline unchanged
until the later restart. Consequently, `remaining_bricks == 1` does not by itself
guarantee that the board contains exactly one eligible tile when last-brick runs.
This ordering exists in the original and the maintained source; both remain
unchanged. There is no new recovered function or exact acceptance.

## Original producer and consumer chain

The connected instructions establish this order:

| Original site | Operation |
| --- | --- |
| `0x40F91F` | Game frame calls the bonus updater. |
| `0x41462F` | Bonus switch word 1 selects `0x414164`. |
| `0x414184` | That branch calls advance-level at `0x415B30`. |
| `0x415B30..0x415BAA` | Set restart/level-changed, advance the index, initialize the new board, and test its count without assigning the live remaining count. |
| `0x411930..0x411961` | Clear auxiliary state and invoke the board loader. |
| `0x40CEA0..0x40CED3` | Copy the selected 400 board bytes into live tile storage. |
| `0x40F959` | Continue the frame through brick effects on the replacement board. |
| `0x40F9F7..0x40FA04` | Test the live remaining count against one and call last-brick. |
| `0x40FED3` | Only later call restart-round. Its positive-lives path invokes reset-round, which assigns the newly counted total. |

Setting restart or end flags introduces no early frame return before the
last-brick gate. Existing effects also survive until that late restart. Their
possible mutation of the replacement board is an additional source-level
qualification; this checkpoint does not execute that connected effect sequence.

The expired last-brick path at `0x415F94` scans columns then rows, accepting
signed tile bytes other than 0 and 2. Every accepted tile overwrites the selected
coordinates and center. Multiple tiles therefore select the last eligible tile
in that scan order. If no eligible tile exists, the stores at `0x41600E` and
`0x416014` never run. Instructions `0x416041` and `0x416045` nevertheless read
the corresponding EBP−12/EBP−8 slots before the call at `0x416049`. The center
slots are likewise assigned only inside the accepted-tile branch.

The existing defined-storage scope for expiry still requires an eligible tile.
The original caller's count test alone cannot establish that scope across a
board transition. Initializing those locals or moving the recount would change
the observed implementation; this investigation makes neither change.

## Retained REA evidence and extents

Pinned REA 6.5.0/Ghidra 12.1.4 inspected the original executable with SHA-256
`756da1ba09edce716d5bf8770320ca0d5ed4e525672b6bb605b9bdb4b88972ba`.
The fresh checkout lacked the previous private dossiers, so this selected family
was re-established in one provider session. Full responses are retained under
`.analysis/rea/`, with original member paths beginning
`runs/2026-10-18T14-58-21.632Z-requests-1947297/`.

| Function | Complete original span | Evidence ID |
| --- | ---: | --- |
| Last-brick `0x415F40` | 1,057 | `ev_d74c65bd4f530ba8aa207b2d9962c5c3db8c028864a61f3e9de34df206c5d0ce` |
| Game frame `0x40F8B0` | 1,688 | `ev_0ed28abee4ca37b0dfe96fa6f00b1ebd59ec0987f5d9c7bcdb58d640756e22d8` |
| Bonus updater `0x413E20` | 2,168 | `ev_0c075d6bb9cda5b8bc39003f62e2e20f89fb24bbdb0c5a837e3f5948957ed2cf` |
| Advance level `0x415B30` | 123 | `ev_92137470c735710e2a5c1fb0095bd6444c5a304cf9d3b0a23f5dbdc93a5225e2` |
| Initialize board `0x411930` | 50 | `ev_3d8a3b02033af697bc62ac814c931169485363120a4c58a1ed5c165c8b445b0d` |
| Count bricks `0x415A90` | 149 | `ev_a61d095ef8332d946eba6a33789c4b149bafe3790ccb4612be5e3663fed98461` |
| Restart round `0x415DF0` | 327 | `ev_602de46b6787ed270f3bdb48ea18d62d14b7ba0bc9a0f3a338fbf3f5e2953bcd` |
| Reset round `0x415C40` | 426 | `ev_2910ead985091cdb7e741215144dbaf569e63ed463c158966942d8ed7fa7420c` |
| Load board `0x40CEA0` | 52 | `ev_0161731225f2b8f1ad3d84f77f8531c3bbc860982462eb0c2e5e3aad9b100668` |

The 6,040 bytes comprise 5,954 imported body bytes, two excluded five-byte
jumps, and the bonus switch's 76 bytes. Direct extraction from the verified PE
corroborates the gaps: `0x40FB21` jumps to `0x40FB35`; `0x414612` jumps to
`0x414677`. All 19 switch words agree with the explicit current match-unit local
bindings. Raw carriers, file offsets and hashes accompany the independent review.
Incoming-reference Evidence
`ev_586c5d9ea6f313985d5696b1416ed427ca9c7cf4bb220150c0c1e469007cdad0`
records the single external direct last-brick caller at `0x40FA04`; unresolved
computed references remain outside that observation.

All ten individual responses completed. Closing snapshot serialization exhausted
the Node heap and ended with `SdkError: Connection closed`; no snapshot was
produced. The scope then became inactive. The complete response records remain
usable with their stated limitations. No successful query was repeated. Resource
samples observed a 403,161,088-byte peak before closure, soft-high reclaim, and
zero sampled hard-max/OOM events; they are not a final whole-run peak measurement.

## Bounded execution and complete comparisons

Three original-only probes execute advance-level, its initializer/loader/count,
and the original memory helpers. Synthetic legal replacement boards contain
zero, one or two eligible tiles. All three retain the previous count of one and
deadline 999. The empty board also sets lives to zero and the end flag.

Each probe then executes the original last-brick prefix with a controlled clock
of 1,000 and no-op sound boundaries, stopping before the explosion queue body.
The empty board passes controlled `0xA5A5A5A5` stack residue as both coordinates;
the two selected slots receive zero writes during that invocation. The other
boards pass `(3,5)` and `(12,2)`, respectively. The original text bytes remain
unchanged. This executes direct calls with explicit boundaries; it does not
establish startup reachability, a full bonus/frame episode, an actual crash,
native C behavior outside its defined scope, late reset execution or gameplay.

One canonical compile per related owner—boards, bonuses, core, display,
gameplay, round and runtime—compares all **69 complete units**, **1,914 actual
code bindings**, **56 complete literal references** and **126 same-section target
checks**. This selection has no attached metadata. All **62 accepted exacts
/ 23,228 code bytes** remain exact. The seven candidates retain their recorded
sizes and differences:

| Address | Function | Original / current bytes | Differing positions |
| --- | --- | ---: | ---: |
| `0x4034F0` | Elapsed | 81 / 81 | 3 |
| `0x40A970` | Animate palette | 234 / 234 | 3 |
| `0x409100` | Present regions | 984 / 984 | 6 |
| `0x409610` | Wait frames | 170 / 170 | 8 |
| `0x415C40` | Reset round | 426 / 426 | 20 |
| `0x412EC0` | Draw paddle | 677 / 677 | 68 |
| `0x415F40` | Last-brick | 1,057 / 1,061 | 992 |

The report is `build/reports/last-brick-family-20261018.json`, SHA-256
`93b5c73f3d3caea68235bf4d97463b99bdba57cbce407590a0766a17806365d3`.
All 43 sealed inputs preserve bytes, modes and nanosecond mtimes. Original and
VC4 identities verify. The comparison takes 17.887 seconds with 383,639,552-byte
scope peak; the probes take 1.325 seconds with 68,464,640-byte peak. Both use one
allowed CPU, 35% quota, 384 MiB high/512 MiB maximum, with zero memory-limit
events. No native build, relink, full replay or game campaign follows.

Global claims remain **475 source-present / 395 exact**, including **250 authored
exacts / 20 authored candidates**. The unresolved last-brick source question is
still its initial sampled-time register/frame representation; this caller review
does not justify another expression, padding or scope trial. Other residual
producers retain their [documented next questions](REMAINING_EXACT_FUNCTIONS.md).

Private `.analysis/last-brick-precondition-20261018/` retains the source review,
independent original/result reviews, input seals, resource receipts and archive
manifest. The verified archive
`.analysis/rea/last-brick-precondition-20261018.tar.gz` preserves the full responses,
probe trace, scripts and compiler products at their original repository-relative
member paths. Current tested objects and the focused comparison report remain.
