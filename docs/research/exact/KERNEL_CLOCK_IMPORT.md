# Genuine Kernel32 clock imports

Updated October 19, 2026. This restores the actual import boundary of
`dxball_current_time` at `0x403450`. It adds no source-present or exact function.
The maintained totals remain 395 exact functions, including 250 of the 270
currently classified authored functions; 20 authored comparisons remain nonexact.

## Original contract and ownership

A new bounded REA session confirms the complete clock entry, its imports and
incoming references. The frequency call at `0x403477` uses the Kernel32 IAT word
at `0x4412A0`; the counter call at `0x4034B9` uses `0x44129C`. Both take the address
of the same eight-byte stack object. The frequency result is a signed 32-bit
BOOL; failure calls `timeGetTime` and returns without querying the counter.
Success caches the unsigned low word divided by 1000. The counter result is
ignored, and its low word is divided by the cached divisor. The high word does
not participate in either calculation.

The complete 148-byte read is the extent authority. REA's instruction listing
omits the unreachable bytes at `0x403492..0x4034A3`; the source retains the
unreachable divisor-zero store after the return. Do not replace that complete
comparison with the shorter listing.

The incoming-reference response includes elapsed, device initialization, intro
frame, waiting, bonus update, level transition and paddle drawing. Their source
call sites do not require a new clock algorithm. Evidence:

- Analysis: `ev_3863f84da077e7414738a60349af0b25765a125304599e951abb46b534b1830d`.
- Full bytes: `ev_5e1acac9534c478a382a6b208e722c1718062bca783aae543b477d38d534420a`.
- Incoming references: `ev_6834dad8a3457bae73dd5e4f85a45d0eb853d352d6f5247848e305b73f6b1c9a`.

Full responses and the saved session are private under
`.analysis/rea/kernel-clock-import-20261019/` and
`.analysis/rea/runs/2026-10-19T05-34-59.145Z-requests-3707050/`.
The session completes under the approved 1 GiB/2 GiB process-tree limits and
256 MiB provider heap: peak 1,074,229,248 bytes, no maximum-limit or OOM event.
The current snapshot retains 91 evidence records and eight primitive cache entries.

## Shared typed source

`src/clock_imports.h` owns the platform projection. Windows uses the pinned SDK's
actual `LARGE_INTEGER`, named `u.LowPart` view and `BOOL WINAPI` declarations.
`runtime.cpp` calls `QueryPerformanceFrequency` and `QueryPerformanceCounter`
directly. The compiled references are genuine
`__imp__QueryPerformanceFrequency@4` and `__imp__QueryPerformanceCounter@4`.
They replace the two synthetic callback-cell references at offsets 41 and 107;
their explicit original targets remain the independently identified IAT words.
The original calling conventions, widths, stack sample and state changes remain.

On the native host the sample type aliases the existing `DxBallCounter` itself.
Real transport functions in `platform_host.c` forward that same pointer through
the live callback cells. There is no copy, temporary counter, union overlay or
aliasing cast. Partial writes, no writes, retained bytes within the invocation,
return status and callback rebinding therefore keep the original native fixture
contract. The default callbacks still consult the live `dxball_clock_ops` table.
The game algorithm is shared between builds.

Windows `current_time` now bypasses overrides of those callback cells and of
`dxball_clock_ops`, as required by the actual imports. Retaining their exports
does not preserve Windows callback interposition. A controlled Windows fixture
must use an actual import boundary. No such fixture or game run is claimed here.

The older [owner-local SDK trial](CLOSED_STORAGE_DIAGNOSTICS.md#current-clock-sample-boundary)
remains historical. Its native union lifetime lacked acceptance; the current
alias and same-object forwarding address that issue without another union model.

## Whole-function comparison and focused checks

One stable VC4 compilation produces the runtime object. The replay initially
stops on changed generated symbol ordinals; the saved object is then compared
without recompilation. All 16 complete functions and 352 actual relocations are
checked. Fifty-seven renamed generated references retain their COFF definitions
and complete containing bytes: 31 string references, 24 internal labels and two
floating constants. Original targets, addends and full literal payloads remain
explicit; the candidate's moved relocation offsets are recorded separately.

All 13 previously accepted functions retain identical raw and resolved bytes,
totalling 2,895 code bytes. `current-time` is still complete 148/148 with zero
differences and nine explicit bindings. The three candidates are:

| Function | Original address | Original / current bytes | Differing positions | Result |
| --- | --- | ---: | ---: | --- |
| `elapsed` | `0x4034F0` | 81 / 81 | 3 | Raw and resolved identity preserved |
| `reset-round` | `0x415C40` | 426 / 426 | 20 | Raw and resolved identity preserved |
| `draw-paddle` | `0x412EC0` | 677 / 679 | 496 | Previously 677 / 677 with 68 differences |

The new declaration context changes the compiler's paddle emission despite its
unchanged source body. Different instruction lengths shift later byte positions;
496 is not a count of missing operations. This regression is retained explicitly:
the genuine import restoration improves source fidelity and loses no accepted
exact function. There is no selective reuse of the old paddle object. Its
remaining sampled-width, bank-address and frame producers still need recovery;
do not start declaration permutations from this compiler effect alone.
The saved before/after object review identifies two one-byte growth sites:
the bank/slot height-address producer at offset `0xBD`, and the dirty-right
sum at old offset `0x206`/new `0x207`. The effective addresses and sum operands
are unchanged; register selection and ADD operand scheduling differ. Thirty-eight
relocation offsets move while their original targets and addends stay fixed.

A separate O2/UBSan native build uses the actual `runtime.cpp` and
`platform_host.c`. Section collection retains only the 11 clock exports and
links with undefined-symbol rejection; no replacement function/data stubs are
provided. Six original/native clock cases pass: disabled fallback, frequency
failure, same-object initialization with live counter-cell rebinding, cached
divisor with live default-table lookup, initialized no-write counter failure,
and noncanonical frequency success. The unmodified original 148-byte body is
executed with only its three IAT targets controlled. Six direct transport cases
check guarded eight-byte objects, pointer identity, partial/no writes and status
forwarding. Both builds and probes share one CPU and the 35%/384 MiB/512 MiB scope;
the native scope peaks at 118,894,592 bytes with no limit or OOM event.

No initial uninitialized sample bytes are observed or compared. A saved sample
pointer is valid only during its owning call. Cached-divisor counter failure
without initialized output and division by zero remain outside these finite
checks. No old semantic matrix is rerun or assigned new cases. Existing ledger
input identities are refreshed through the documented native compatibility
chain; they are not new Windows or full-game acceptance.

Current private authority: `.analysis/kernel-clock-import-20261019/`, including
`comparison.json`, compiler inputs/resource receipt, native build and boundary
receipts, ledger refresh and independent review. The older linked delivery has
not been relinked with this or the preceding word-arithmetic changes.
The closed evidence archive is verified member by member before copied input
trees, the previous runtime object and disposable native probe products are
deleted. The current canonical runtime object and logs remain available.
