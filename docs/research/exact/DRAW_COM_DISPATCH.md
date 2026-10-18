# DirectDraw method-slot and argument-frame correspondence

The October 18 follow-up maps **128 original register-relative calls across
62 game functions** to the maintained DirectDraw source sites. Together with
the [49-site sound proof](SOUND_COM_DISPATCH.md), all **177 register-relative
calls** from the declared-prefix review now have source method-slot associations.
The [128-row site ledger](DRAW_COM_SITES.csv) records original addresses, source
lines, receiver expressions, argument frames and native REA Evidence identities.

This is a static call-site correspondence. Each function's source-call count
and order agree with the original register-relative call count and order, and
every vtable offset agrees with the typed source method. The original receiver
and pushed `this` expressions agree at all 128 sites. There are 558 argument
positions including `this`: 126 frames have bounded straight-line setup; two
require the original nested-callee contracts described below.

## Observed interfaces and receivers

| Typed interface | Sites |
| --- | ---: |
| `IDirectDraw` | 19 |
| `IDirectDrawSurface` | 98 |
| `IDirectDrawPalette` | 9 |
| `IDirectDrawClipper` | 2 |
| Total | 128 |

All device, palette and clipper receivers load their existing cells at
`0x4228B0`, `0x4228C0` and `0x4228C4`. Surface receivers comprise 74 fixed-cell
loads, twelve incoming surface arguments and twelve sprite-bank/sprite loads.
The fixed cells are primary `0x4228B4`, secondary `0x4228B8`, board `0x4228BC`,
active `0x4265CC`, effect `0x42E690` and background `0x421070`. Their existing
explicit relocation bindings supply the maintained symbol names.

The symbolic reader stays within the current basic block, stops at sparse
listing gaps and direct branch targets, and follows actual MOV/LEA/DWORD
arithmetic producers. It does not carry inferred memory values through calls.
All 126 simple contexts have the required pushes and no intervening call,
POP, LEAVE, ENTER or explicit ESP mutation. Absolute calls are excluded only
after their cells are checked against the original named PE imports.
Retained instruction operands agree with original-byte decoding after narrow
32-bit effective-address and scale-one normalization. This normalization is
not a general instruction-equivalence checker.

## Two nested scroller frames

The calls at `0x407C37` and `0x407C79` belong to `dxball_draw_scroller_wave`
at `0x407BA0`. Each begins by pushing BltFast flags, rectangle address and
source surface. It then pushes a temporary sine argument, calls `0x402400`
and explicitly removes that argument with `ADD ESP,4`. After multiplication
by the original double constant 20.0, it calls conversion helper `0x41678C`.
The eventual six method arguments are:

| Position | Original expression |
| --- | --- |
| `this` | Primary `0x4228B4` or effect `0x42E690` cell |
| X | Current cursor at `[EBP-8]` |
| Y | Low EAX result of the conversion call, plus 420 |
| Source | Board surface loaded from `0x4228BC` |
| Rectangle | Address `EBP-24` |
| Flags | `0x10` |

New original dossiers cover all 130 sine bytes and all 39 conversion-helper
bytes. Both use a preserved frame pointer and end in LEAVE followed by plain
RET. Sine writes its own argument at EBP+8 and local storage; it does not
write the pending outer arguments starting at EBP+12. The conversion helper
takes x87 ST(0), writes a qword local, restores the control word and returns
that local in EDX:EAX. It has no stack arguments or nested call. Thus the three
earlier method arguments remain on the caller's stack during normal returns.
The conversion result remains symbolic; no numeric or exceptional-path
execution is inferred.

Ghidra combines bytes `9B D9 7D FE` at `0x416792` into FSTCW; Capstone exposes
WAIT followed by FNSTCW at `0x416793`. This instruction-boundary difference is
explicitly reconciled within the same complete 39 bytes. The checker also
accounts for x87 stores omitted by Capstone's generic access metadata and
checks their sizes against the actual local-frame bounds.

| Callee | New original Evidence |
| --- | --- |
| `0x402400`, sine | `ev_636b01bd912cc7efa9e1f19de3d929465acaf4b35d87877034e16fc50783c21b` |
| `0x41678C`, conversion helper | `ev_0c6e54fdeff7f1eb7cad8fe814fe7301bb90db1c0cf9592aa8d32f465595eaae` |

## Scope and remaining reconstruction

Of the 62 call-bearing functions, 51 have accepted exact comparisons and eleven
remain authored candidates. This pass does not recompile them or prove that
every source argument value equals its original counterpart. Source-order
associations, symbolic frame expressions and whole-function exactness are
distinct claims. The stronger sound proof independently compares all 17
complete sound units; it is retained separately.

Across both site ledgers there are 177 distinct original call addresses in
74 functions and 659 argument positions. No additional authored-function
hypothesis arises from this method-slot association, but concrete live COM
implementation addresses, object validity, API success, lifetimes, alias
closure and the final authored-function denominator remain open. The current
authored totals stay **270 source-present, 250 exact and 20 candidates**.

The 62-query session closes in 149.325 seconds; the two-callee follow-up closes
in 154.238 seconds. Both use CPU35%, one CPU, the approved 1/2 GiB scope and
the 256 MiB Java heap. Their peaks are 1,074,196,480 and 1,074,257,920 bytes;
soft-high events are 1,379 and 1,465, with zero max/OOM events in both.
The cumulative snapshot now contains 80 Evidence records. Complete raw
responses, request/resource receipts, rejected reader proposals and independent
reviews remain under `.analysis/rea/draw-dispatch-20261018/`,
`.analysis/rea/draw-nested-call-20261018/` and their immutable REA run directories.
The independent forward check verifies all 128 frames, 558 arguments, 1,788
unique context instructions and 81 excluded named import calls. The closed
proof is sealed in `.analysis/rea/completed-draw-dispatch-20261018.tar.gz`;
all 145 members verify by size and SHA-256. After verification, 69 identical
result aliases are removed, releasing 10,051,584 allocated bytes. The current
80-record snapshot and immutable responses remain available.
No game probe, full campaign or new exact-function acceptance follows.
