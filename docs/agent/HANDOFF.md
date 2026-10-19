# DX-Ball reconstruction handoff

Updated October 19, 2026. The reconstruction is unfinished. Recover the English
DX-Ball v1.07 functions as exactly as possible, as readable shared C/C++;
then verify the original VC4 build and playability; resume ports after that.
The user permits the **19 explicit original CRT members** in the restored-CRT
delivery. Removing them is not a delivery gate. Prioritize authored functions.

Paths below are relative to the repository root. Read [AGENTS.md](../../AGENTS.md),
[WORKFLOW.md](WORKFLOW.md) and the selected owner note before changing source.
Keep code, tracked documentation and commits English. Keep the README focused on
the reconstruction approach and REA, with its two centered 900px images.

This file describes current decisions and open work. The detailed
[handoff at c99ab9e](https://github.com/N0zoM1z0/dx-ball/blob/c99ab9e62fcc1625a0c0754a3ee0abb67dc10623/docs/agent/HANDOFF.md)
retains the preceding adoption and cleanup chronology. Owner notes and private
receipts remain authoritative within their stated scopes. Historical totals
are not current totals.

The user resumed reconstruction on October 18. The native checkpoint
completes the interrupted DirectSound queries and the DirectDraw follow-up:
all177 register-relative sites now have native source-method/slot associations
and reconstructed argument frames, without changing game source.
The subsequent complete resource address-order control is rejected:three
private gains lose four prior exacts. A fresh restored-CRT build now produces
a locally present 166,400-byte EXE and covers all 270 authored comparisons,
preserving 250 exact/20 nonexact. No game process runs. Continue authored
recovery; the short startup check has concrete environment prerequisites below.

The preceding [raster arithmetic correction](../research/exact/RASTER_WORD_ARITHMETIC.md)
changes three shared source bodies to preserve native 32-bit word operations.
Six original/native additions and four polygon entry/cases pass, with two
old-source UBSan failures confirming the corrected boundary defects. All twelve
whole raster units are compared: nine exacts survive, triangle is now 1710/97,
ordinary 1543/216 and clipped 1592/216. No new exact or source entry is claimed.
Historical raster vectors are not rerun; the recorded compatibility chain refreshes
input identities without adding cases. Private current comparison:
`.analysis/raster-word-arithmetic-20261018/comparison.json`.

The latest [word-width recovery](../research/exact/WORD_WIDTH_BOUNDARIES.md)
corrects signed source-row displacement in rotation and modular text measurement.
Four original/native signed-pitch pairs and five text-width cases pass, with
isolated old-source failures confirming both defects. Twelve complete VC4 units
retain every prior raw/resolved code identity, including ten exacts/1,796 bytes.
Renderer remains 1458/1572 with 1,466 differences and measurement 279/279 with three.
No exact/source count increases or full-game validation is claimed. Reuse
`.analysis/word-width-recovery-20261018/comparison.json` and the scoped boundary
proofs; do not repeat historical matrices.

The latest [Kernel32 clock integration](../research/exact/KERNEL_CLOCK_IMPORT.md)
restores genuine frequency/counter imports and a same-object native transport.
One runtime compile and saved-object comparison cover all 16 whole functions,
352 bindings and 57 generated references. All 13 accepted exacts/2,895 bytes
retain their identities; current-time remains 148/0, elapsed 81/3 and reset
426/20. The unchanged paddle body now emits 679 bytes/496 differences instead
of 677/68; this declaration-context regression is retained explicitly, without
using the old paddle object. Six original/native clock cases and six guarded
transport cases pass in an O2/UBSan build of the two actual owners. Windows
current-time now uses real imports and bypasses callback-cell/table overrides;
native overrides retain pointer identity and live lookup. No exact/source count
increase, historical matrix rerun, delivery relink or game execution is claimed.
Reuse `.analysis/kernel-clock-import-20261019/comparison.json` and its scoped
boundary receipts. REA completes with the approved 1 GiB/2 GiB limits, no OOM.
The private `closed-evidence.tar.gz` and `archive-receipt.json` preserve and
member-hash verify the old/new inputs, objects, probes, reviews and REA snapshot
before disposable copies and native probe products are removed. The canonical
VC4 runtime object/log, old linked delivery and useful caches remain.

## Current authorities

| Inventory | Current value |
| --- | ---: |
| Provisional independent entries | 553 |
| Retired parent-owned compiler-fragment rows, counted separately | 24 |
| Source-present entries | 475 |
| Accepted complete exact functions | 395 |
| Exact code / attached metadata bytes | 85,106 / 244 |
| Complete nonexact comparisons | 80: 20 authored / 60 runtime / 0 generated |
| Scoped semantic ledger rows | 249 |
| Entries without source | 78: 77 runtime / 1 generated |
| Inventory origins | 270 authored / 261 runtime / 21 generated / 1 unknown |

All 270 classified authored entries have source and complete current comparisons:
250 exact and 20 candidates across 30 compiler closures. The source-present
16-byte no-op at `0x40CC20` remains origin/prototype-unknown. Neither the final
authored denominator nor source optimality has been established. These inventories
are separate claims, not interchangeable completion percentages.

| Authority | Purpose |
| --- | --- |
| `config/functions.csv`, `function-origins.csv` | Provisional entries, reconciled extents and origins |
| `config/compiler-fragments.csv` | Retired aliases owned by complete C++ parents; not every internal block |
| `config/implemented.csv`, `matches.csv`, `semantic-acceptance.csv` | Source, exact and scoped semantic claims |
| `config/source-owners.toml`, `match-units.toml` | Source ownership; full compiler recipes, extents and bindings |
| `build/reports/exact-replay.json` | Last global 395 accepted comparisons and producers; historical private receipt |
| `build/reports/last-brick-family-20261018.json` | New local 69-unit check: 62 exacts and seven unchanged candidates |
| `build/reports/resource-family-20261018.json` | Local canonical 18-unit baseline: 13 exacts and five unchanged candidates; address-order proposal rejected |
| `.analysis/fresh-restored-build-20261018/matching-comparison.json` | Fresh delivery objects: 353 new whole comparisons and 104 reconciled results; 386 exact/71 candidate units |
| `.analysis/fresh-restored-build-20261018/coverage-review.json` | All 270 authored functions covered; 18 global runtime units excluded from this delivery comparison |
| `.analysis/kernel-clock-import-20261019/comparison.json` | Current runtime object: 13 exacts and three candidates; supersedes runtime results in the fresh delivery report |
| `.analysis/exact-candidate-audit-20261012/comparison.json` | Historical 80-candidate base; later owner reports supersede changed results |
| [Remaining-functions table](../research/exact/REMAINING_EXACT_FUNCTIONS.md) | All candidate results and owner-note links |
| `.analysis/kernel-clock-import-20261019/authored-table-review.json` | Current 270 authored ledger entries/30 closures and all 20 table results reconciled against retained owner reports |

Original `original/DXBALL.EXE`: English v1.07, 158,208 bytes, SHA-256
`756da1ba09edce716d5bf8770320ca0d5ed4e525672b6bb605b9bdb4b88972ba`.
The pinned compiler is VC4 10.00.5270 and linker 3.00.5270; original CRT provenance
uses `.tools/msvc400/lib/libc.lib`. The compiler identity is
`f097e736bb04d38391c8b524945d58809ec4c42e97c056eca6f40bba2de910c3`.
Original compiler settings cannot be inferred solely from this candidate toolchain.

Keep `original/`, `.tools/`, `build/`, `.analysis/` and `ghidra-project/` private.
A source-only clone does not include the assets, tools, products or raw evidence.

## Current source and delivery

Current locally rebuilt delivery: `build/vc40-restored-crt/dxball.exe`, 166,400
bytes, SHA-256 `682cfc7fdf288b185bd4d5880b0d6790dc489eb4cfb9ea390166ad79a2bcb4e8`.
The [fresh build proof](../research/RESTORED_CRT_GAME_ENTRY.md#fresh-reconstruction-build-october-18)
records 109 compiles/nine verified reuses and scoped static final-link checks.
The historical 40f92f0f delivery is not locally available for a complete binary
comparison; its earlier validation remains historical.
The [genuine MulDiv integration](../research/exact/EXACT_FIXED_POINT.md#genuine-api-integration-october18)
precedes the latest raster word-arithmetic correction. Its native/Windows/both
VC4 builds,
7,164 existing raster cases, complete linked containers and 4,488 loader fields
pass within that checkpoint's scope. That link reused 118 objects and 19 approved
original CRT members. The fresh rebuild retains that checkpoint's source and
recipes with its own product identities. The later arithmetic and clock checkpoints compile their changed
owners separately; the EXE above has not been relinked with those source changes.

Relevant accepted source contracts:

- [Independent board storage](../research/exact/INDEPENDENT_BOARD_STORAGE.md)
  preserves seven real objects, two mutable unknown slots, the real list word
  at +0xC, natural pointer widths, ordered linker sections and retained memmove.
  The 20,432-byte layout and 368-byte terminal overlap are ABI observations;
  the descriptor is a view, with no enclosing instance or ISO array-bounds claim.
  Adoption promoted17 complete units and demoted eight; do not hide those losses
  with old objects or selective header variants.
- [Score workspace](../research/exact/INTRO_SCORE_PHASE.md) and
  [score strip](../research/exact/SCORE_STRIP_SOURCE.md) capacities follow real
  consumers and independent workspace regions. They do not justify padding in
  unrelated functions.
- [Paddle sampling](../research/exact/PADDLE_WIDTH_SAMPLING_SCOPE.md) preserves
  the sampled width and dirty-right sum; its complete body remains677/68.
- Bank loading preserves callback-visible state, partial failure ownership,
  and the pitch snapshot before Lock. Keep the Windows allocation-mode argument
  and COM behavior; foreign Image/backend records are different.
- Keep the documented GNU C++17/x87/excess-precision options for `balls.cpp`,
  C linkage, real Win32 heap/raster defaults, and stdio-before-onexit ordering.

## Last closed work

The fresh restored-CRT build completes without compiler/linker errors. Full
original-address comparison covers all 270 authored functions and 187 other
units, with no accepted regression or new promotion. Nine runtime owners/18
units remain outside the delivery comparison; do not call this a new 395-unit
global replay. Static final-link checks verify 578 complete sections and 4,090
of 4,488 loader fields, retaining 398 unbound fields, 407 unlocated sections and 59
sections with unresolved destinations. Private
`.analysis/fresh-restored-build-20261018/` retains exact binding/coverage limits.
The prepared runtime has 48 exact data copies; all 49 originals verify unchanged.
No game runs: `xdotool`, ImageMagick capture commands, 32-bit audio libraries
and `dxball_reconstruction_silent` are absent. Establish those prerequisites
before a short original/rebuilt startup control; no full campaign is queued.
Source, exact/semantic ledgers and progress counts stay unchanged.

The [fixed resource address-order control](../research/exact/RESOURCE_ROTATION_WRAPPER_OWNER.md#fixed-address-order-resource-control-october-18)
first recreates the locally absent canonical object:18 complete functions,
13 exacts/3,050 bytes,262 bindings and six full literal references. One fixed
definition-order proposal then restores draw/blt/release sprite but loses keyed
draw/stretch and glyph find/draw, giving12 exacts/2,895 bytes. Reject it whole;
all13 sealed inputs/authorities restore and the canonical baseline object stays
current. No subset or further position/header variants are queued. Source,
ledgers, delivery identity and250 authored exact/20 candidates stay unchanged.
The private `.analysis/resource-address-order-20261018/` contains both complete
comparisons and explicit actual-symbol/literal mappings. The related
[polygon source check](../research/exact/POLYGON_SCAN_WORKSPACE.md#additional-bounded-source-comparison-october-18)
excludes one primary Abrash implementation after16 bounded search queries;
it establishes no new declaration. Reuse these closed results.

The [DirectDraw follow-up](../research/exact/DRAW_COM_DISPATCH.md) adds128 native
site associations across62 functions. All receiver/this expressions agree;
126 simple frames and two explicitly proved nested sine/x87 frames account
for558 argument positions. Combined with sound:177 distinct sites,74 functions
and659 argument positions. Count/order/slot and frame correspondence does not
prove whole nonexact bodies or all source argument values. Concrete live COM
targets, validity/lifetime/alias claims and the final authored denominator stay
open. 51 call-bearing draw functions are accepted exacts and11 remain candidates.

The two focused callee dossiers establish sine402400's130-byte normal-return
frame and ftol41678C's39-byte x87/EDX:EAX frame, with plainRET in both. The
existing approved CRT catalog entry gains machine-interface/extent evidence;
its source/status/counts stay unchanged. The cumulative native snapshot now
has80 Evidence records. Reuse `.analysis/rea/draw-dispatch-20261018/` and
`.analysis/rea/draw-nested-call-20261018/`; no compiler or game runs. The
closed draw archive has145 member-hash-verified files;69 redundant aliases
are removed after verification, releasing10,051,584 allocated bytes. Current
snapshot and immutable responses remain. Tracking validates553 candidates,
475 source-present entries and395 exact functions. The
[20-candidate table](../research/exact/REMAINING_EXACT_FUNCTIONS.md#authored-candidates)
now pairs every unchanged full comparison with its next unresolved evidence
question. Equivalent spelling and declaration sweeps remain closed.

The [DirectSound dispatch review](../research/exact/SOUND_COM_DISPATCH.md)
closes the failed native batch under the larger REA memory budget. Fifteen
queries succeed; the session reuses the initialization dossier and closes with
16 cumulative Evidence records. All49 sound register-relative calls have
original-site/source/slot/receiver/argument correspondence, with445 setup
instruction occurrences and101 argument pushes checked. The actual factory
thunk416606 targets IAT441234; the helper's observed caller forwards the live
record's buffer output at offset zero. Three global-xref lists retain their
exact-address scope. Concrete live method destinations and alias/lifetime
claims remain open. The later draw review above supplies the other128 sites
under its own correspondence scope.

The unchanged sound compile compares17 complete functions/4,756 exact bytes,
235 actual bindings and12 full literal references. Reuse
`build/reports/sound-dispatch-20261018.json`, the current sound object and the
sealed16-record sound snapshot; the current `.analysis/rea/dxball.snapshot.json`
now has80 records. Do not recompile unchanged inputs. Private
`.analysis/rea/sound-dispatch-resumed-20261018/` retains the
native join and resource receipt. No source, match count or game acceptance
changes. The completed sound archive has140 member-hash-verified files and29
unchanged protected inputs;20 redundant aliases are removed after verification,
releasing10,264,576 allocated bytes. Current products, snapshot and immutable
run records remain. The progress generator now explicitly reports270 authored source
entries/250 exact/20 awaiting exact matches, with the denominator provisional.

The [last-brick transition review](../research/exact/LAST_BRICK_TRANSITION_BOUNDARY.md)
confirms that a level-skip bonus replaces the board before the last-brick gate,
while the old remaining count and deadline survive until late restart. Therefore
the count-one gate alone does not establish an eligible tile. Nine original
spans/6,040 bytes reconcile through REA plus two excluded jumps and the complete
19-word bonus table. Three original-only direct-call probes retain the stale
count on zero/one/two-tile replacements; the empty expired scan reads unwritten
coordinate slots. They stop before the explosion queue body. Preserve this
original behavior; there is no full-frame reachability or crash claim.

Seven unchanged owner compilations compare 69 complete units/1,914 bindings/56
full literal references: all 62 prior exacts/23,228 bytes and seven candidate
sizes/difference counts survive. The new focused report is
`build/reports/last-brick-family-20261018.json`; private reviews and receipts are
under `.analysis/last-brick-precondition-20261018/`. No source, exact or semantic
acceptance count changes, native build, relink or campaign follows.

This fresh checkout initially lacked historical `.analysis/`, `build/` and
Ghidra projects. The older receipt/delivery identities elsewhere in this handoff
remain historical authorities, not locally present products. Pinned Node 22.19.0
is now in `.tools/node-22.19.0/bin`; a private Ubuntu Wine 9 compiler runtime is in
`.tools/wine9-private/bin`. Prepend the relevant directory to PATH inside the
required systemd scope. The original VC4 compiler/linker banners verify. Wine
gameplay/audio support is untested. The initial REA session completed all ten
individual responses but exhausted Node heap during closing snapshot serialization;
no snapshot was produced. Its scope exited, full responses were archived and
member-hash verified. The later approved memory-budget and native checkpoints
above supersede that failure; the current80-record snapshot is retained.

An independent source-only inventory under
`.analysis/com-call-inventory-20261018/` identifies 177 COM call sites across 74
catalogued functions: 128 DirectDraw-family and 49 DirectSound-family. The later
native reviews above establish site/slot/frame correspondence for all177 and
close the factory/caller/device query. Concrete live destinations and lifetime
claims remain open. Do not repeat those queries or infer a final authored
denominator from the source-site count.

The [bank filename and path review](../research/exact/MAC_CANDIDATE_FLOW_CONNECTIONS.md#bank-filename-qualification-and-path-boundary)
reads one previously missing416-byte Mac helper through REA6.5 process capture
of the saved Ghidra project. All104 instructions,18 branches and six calls are
accounted for. Direct nonstack writes use a separate pointer loaded through r2;
input/output aliasing and four callee effects remain unknown. This does not
recover the Windows qualifier or prove mutable input.

One fixed filename/callback qualifier inference then receives one resource
compile. All18 complete raw/resolved bodies,262 bindings and six full literals
remain identical;13 prior exacts/3,050 bytes survive. Both complete12,332-byte
COFF files differ only in timestamp bytes4–5. Bank remains1475/64. Reject the
whole model; keep the canonical const API. The other27 owners/254 functions
remain uncompiled and unknown for that proposal. All754 protected SHA/mode/
nsmtime identities restore. No native build, relink, game or full replay follows.

The compiler/restore/comparison pipeline takes4.795s, peak193,404,928 bytes,
zero memory-limit events. The saved-project capture peaks403,165,184 bytes,
767 soft-high events and zero max/OOM events. Both use CPU0/35%,384/512MiB.
The verified33-member archive removes two temporary objects, seven proposals
and closed capture/runner inputs, releasing729,088 allocated bytes net.
Current products, useful caches, the saved project and selected helper export
remain. Private receipts:

- `.analysis/bank-filename-qualifier-20261018/`: eligibility/plan/result reviews,
  `summary.json`, `restoration.json`, `protected.json`, `archive-manifest.json`,
  `cleanup.json`, and `closed-model-and-path-capture.tar.gz`.
- `.analysis/mac-path-contract-20261018/`: question, complete selected export,
  process resource receipts and `independent-path-contract-review.json`.
- Capture Evidence `ev_acd98536850530d1f826c778dcdfaea0a33588ea746708b4111168ceaf0ce64c`.
  Full process Evidence is inside the verified archive, not a native snapshot.

Other recent closed models are indexed in
[Mac candidate flows](../research/exact/MAC_CANDIDATE_FLOW_CONNECTIONS.md) and
[fixed-point notes](../research/exact/EXACT_FIXED_POINT.md): bank API names,
paddle float-input precision, line public name, score parameter kind, and the
paired triangle/span DWORD colour declaration. The colour model regresses both
polygons while preserving ten other bodies; reject the whole model. The score
parameter model regresses paddle. Do not repeat these trials or widen them in
response to their outputs. The bounded polygon source-index lookup returned
zero matches with shard limits; it does not prove source absence.

## Resuming authored recovery

Start with the current [20-function table](../research/exact/REMAINING_EXACT_FUNCTIONS.md#authored-candidates),
`config/functions.csv`, the relevant owner note and retained complete evidence.
Missing original declarations are reconstruction work, not an external blocker.
Form one bounded inference from actual producers, consumers, ownership or layout;
unique historical spelling is not required. A small byte-difference count alone
is not a new source question. Keep inference separate from recovered fact.

| Family | Reuse before another proposal | Boundary to preserve |
| --- | --- | --- |
| Bank/resources | [Bank flow and closed controls](../research/exact/MAC_CANDIDATE_FLOW_CONNECTIONS.md#reused-bankshape-bodies-and-api-name-control), current frontend/backend traces | Bank1475/64 already restores extent/yoffset; names, filename qualification, cursor/row/column and transfer scopes are closed |
| PCX | [Complete packet proof](../research/exact/EXACT_PCX_PACKET_LOOP.md), [storage diagnostics](../research/exact/CLOSED_STORAGE_DIAGNOSTICS.md) | Original862/current979; all227 instructions accounted. Current308-byte frame has305 typed bytes plus3 slot padding. Original unaddressed four bytes do not justify a132-byte header or fake local |
| Triangle/polygons | [Fixed-point](../research/exact/EXACT_FIXED_POINT.md), [polygon workspace](../research/exact/POLYGON_SCAN_WORKSPACE.md) | Four root FixedPoint constructions/EH states;28-byte edge has one unknown word at+12. Preserve paired accesses, three pools, both Shellsorts and signed negative-error carry |
| Rotation | [Pixel-address correspondence](../research/exact/ROTATION_PIXEL_ADDRESS.md) | All365 instructions/22 calls/26 branches accounted. Unknown80-byte frame difference is not permission to add padding; integer-offset-before-base order is restored |
| Line/ranking/presentation | [Line](../research/exact/LINE_LOCKED_CURSOR.md), [ranking](../research/exact/RANKING_OWNER_FAMILY.md), [presentation](../research/exact/PRESENTATION_MERGE_SCOPE.md) | Known comparison/register producers remain. Fixed line rank model restores directions but loses correct homes; ranking has original homes and one shorter compare producer |
| Clocks/palette/last brick | [Kernel imports](../research/exact/KERNEL_CLOCK_IMPORT.md), [author context](../research/exact/AUTHOR_SOURCE_CONTEXT.md), [lightning crop chain](../research/exact/EXACT_LIGHTNING_CROP_CHAIN.md) | Clock cache/sampling order accounted; genuine imports retained. Paddle now679/496; two equivalent producers grow one byte each. Keep clock before RNG and existing native callback-visible state |

Resource callback-table extraction and historical DirectDraw header controls
can produce a private exact release-sprite while losing prior exact companions.
Those models remain rejected. Full-owner C/C++ and broad declaration controls
are also closed. Avoid name/order/count/flag sweeps, fake unused storage, assembly,
per-profile bodies, selective old objects, and repeated unchanged controls.
The [historical handoff](https://github.com/N0zoM1z0/dx-ball/blob/c99ab9e62fcc1625a0c0754a3ee0abb67dc10623/docs/agent/HANDOFF.md)
and linked owner notes retain the detailed boundaries of older trials.

## Reusable evidence and runtime limits

[REA](REA.md) is pinned at6.5.0/Ghidra12.1.4. The old MCP catalog can still report6.4;
use fresh `scripts/rea` CLI calls. Reuse closed evidence before opening a provider.
Native PEF admission is unsupported. Retained Mac observations use REA process
capture of pinned Ghidra; no native-provider snapshot or runtime r2/TOC model is
established. Use corrected `PowerPC:BE:32:default` exports with r2 unset.

Useful private Mac paths are `mac-port-payload-20261018` (carrier and321 named
traceback records), `mac-pef-focused-bodies-20261018` (corrected17-body export),
`mac-candidate-bodies-20261018` (loaded data/relocations/symbols), and the later
candidate-flow/score/path review directories, all under `.analysis/`.
The loaded645,276-byte data image is static loader evidence. Keep original
failed/wrong-width records separate. Reuse sealed compiler C1/C1XX/C2 snapshots
and traces; cold imports are expensive and do not recover original declarations
by themselves. [Frontend symbol order](../research/exact/VC4_FRONTEND_SYMBOL_ORDER.md)
and [backend records](../research/exact/VC4_BACKEND_SYMBOL_RECORDS.md) explain their limits.

[CRT dependency receipts](../research/exact/CRT_DEPENDENCY_INVENTORY.md#complete-receipt-coverage)
cover all78 no-source entries;19 original member dependencies are approved.
Do not divert authored recovery into fake C implementations of x87/SEH/stack
probe transports. Joined text/direct-flow audits retain their bounded scopes;
177 register-relative call values remain unresolved and the final authored
inventory is not established.

Earlier [entry/exit evidence](../research/RESTORED_CRT_ROUND_FLOW.md#current-image-bounded-entry-and-exit)
passes a bounded board0 episode on an earlier image. The historical
[original50 campaign](../research/ORIGINAL_CAMPAIGN.md#current-restored-crt-original-bank-prefix-october-17)
ended at its14,400s deadline after verifying initial boards0–19. It did not
complete50 or establish a crash/normal application exit; never restart that
producer. Custom single-brick boards and prior GUI episodes retain their own
image identities. Physical Windows, graphics/audio fidelity, exceptional paths,
full campaign acceptance and Wine9
[focus/surface-loss](../research/ROUND_FOCUS_RUNTIME.md) remain open.
No new game acceptance is claimed for the current image. Ports remain deferred.

## Execution, cleanup and publication

Use `scripts/repo-python`, bounded LeanToken source reads, one allowed CPU and
one writable compiler/provider/Wine session. `session_lock()` is non-reentrant;
do not wrap a helper that already acquires it. CMake uses `--parallel 1`.
REA commands run in a user scope:

```bash
systemd-run --user --scope --quiet \
  -p CPUQuota=35% -p MemoryHigh=1G -p MemoryMax=2G \
  scripts/rea session path/to/requests.json
```

Compiler/Wine commands and standalone passive readers retain the 384/512MiB
scope. The user approved the larger REA memory budget on October 18 after
the 384/512MiB scope repeatedly pressured REA startup despite available host RAM.
Earlier receipts retain their original limits. CPU affinity, quota and serial
execution remain unchanged. One native query of `0x405120` completes and saves
its snapshot in130.134s, with peak1,074,053,120 bytes,492 soft-high events and
zero max/OOM events. Reuse `.analysis/rea/memory-budget-20261018/` and its
seven-member verified archive; [REA commands](REA.md) records its Evidence ID
and comparison with the previous failed startup. No match count changes.
REA's Java heap cap is256MiB; the saved Mac project queries use128MiB and
Node192MiB. Do not overlap heavy trees. Automated audio uses
`PULSE_SINK=dxball_reconstruction_silent`; never change the default sink.

For a genuine new source model, verify the relevant target/toolchain, freeze
previous products and all recursive inputs, compile once per stable family,
and compare complete affected candidates and accepted companions. Include
all actual relocations, local destinations, full literals and metadata.
Restore canonical bytes, modes and nanosecond mtimes in `finally` under the lock;
verify Toolchain on both sides, including failures. Own child process groups
before restoring parent signals; unblock inherited signals in workers. Cleanup
ignores repeated TERM/INT, uses TERM plus bounded communicate, then unconditional
KILLPG and wait even if the group leader exited. A timeout preview is not a
reason to restart a still-live producer.

No default full replay, historical Oracle queue or repeated unchanged game run.
Update only changed claims; the handoff cleanup changes no ledger or progress
count. Current tested native/exact/VC4 products, useful incremental caches,
originals, manual saves and saved Ghidra project remain private and retained.
The20 existing probe/reference files inspected during handoff include reusable
readers and unique evidence; none is blindly deleted.

Archive unique closed evidence, verify every member's size/SHA, then remove only
the exact reviewed list. The latest archive/member hashes and allocated-byte
accounting are in the cleanup receipts above. Older historical raw paths may
have verified `.json.gz` carriers; check their original decompressed seals.
Never hardlink mutable products or aliases to immutable archives. The general
`scripts/clean-local.py` defaults to preview; inspect its proposed scope before
using `--apply`. Do not recursively remove evidence, tools or current caches.

Publish verified checkpoints to `origin/main` with an English subject beginning
`gpt-6.1-sol: `. Disable opportunistic Git GC/maintenance, verify raw commit message
bytes against the prepared message, check the remote with `git ls-remote`, and
finish with a clean worktree. A tidy handoff or complete source coverage does not
mean reconstruction is complete.
