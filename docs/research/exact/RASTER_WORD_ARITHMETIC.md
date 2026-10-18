# Raster word arithmetic, October 18

The shared raster source now preserves two original 32-bit operations beyond
its earlier representable-arithmetic domain: FixedPoint accumulation and the
negative-edge error comparison in both polygon controllers. This corrects
three existing implementations; it adds no source-present entry or exact match.
All nine accepted raster functions remain exact. The triangle and both polygons
remain candidates, with the complete current results below.

## Native observations and source

The full 110-byte operator at `0x0040B450` adds the by-value operand to the
receiver with `ADD DWORD [ECX],EAX` at `0x0040B47E`. No overflow flag is consumed
before the result is used. The normal path returns the same receiver, destroys
the by-value operand and restores SEH before `RET 4`. The original has eight
resolved call sites in the triangle. This establishes its word arithmetic and
ABI, not historical identifier spelling or overflowing gameplay inputs.

The source accesses the existing signed member through its corresponding
unsigned type:

```cpp
reinterpret_cast<DxBallUInt &>(value) += (DxBallUInt)increment.value;
```

C++ permits this signed/unsigned alias. Both the addition and write operate on
an unsigned 32-bit word; no extra storage, copied instructions, lifetime change
or alternate implementation is introduced. Signed consumers retain the supported
targets' two's-complement representation. A first RHS-only unsigned conversion
emitted 115 bytes and lost the original memory-ADD producer; that complete
proposal is rejected and retained privately. The adopted operator is 110 bytes
with zero differences, including its complete 40-byte exception metadata.

The complete ordinary/clipped polygon listings have 458/468 instructions.
They add `dx` to error at `0x0040BAAD`/`0x0040C0EE`, select the negative branch
with a signed comparison, and negate a loaded error word at
`0x0040BAC3`/`0x0040C104`. The subsequent `CMP` replaces NEG's flags before
signed `JL` at `0x0040BACB`/`0x0040C10C`. Thus `INT_MIN` stays `INT_MIN` under
negation; no overflow trap or saturation is present. Both source comparisons
now use `(DxBallInt)(-(DxBallUInt)work.edge->error)`. The outer signed conversion
is essential to preserve the comparison. Its bit mapping is supported by the
selected targets, not a claim about every possible C++ signed representation.
All other coordinate, edge-carry, allocation and pointer bounds remain.

REA 6.5.0/Ghidra 12.1.4 evidence, retained in full under `.analysis/rea/`:

- Operator dossier: `ev_ce096b028fe0ef992daf9ef14ce3d3f2aad2ecf919681a7e781a1f93801639e5`.
- Complete 110-byte read: `ev_460fe2180f5df49d29aa6e56b37d0c371b0654ae83f28fcf161910c7f54fb787`.
- Incoming references: `ev_fd4ecb85b34a16ea554ee4ec068ce492fa6c07649744380e3f6ebabb03288dfa`.
- Ordinary polygon: `ev_7b7adf3ceb744a93a4998298d121c97e1cfadcb1574bbf35a80153d87944740e`.
- Clipped polygon: `ev_07b2bad856a682d0792661a586dc257623bd2151081294871f8420ca08113145`.

Both sessions close successfully, extend the saved snapshot to 86 records,
and record no OOM/max-limit events under the approved 1 GiB high/2 GiB maximum.

## Complete compiler comparison

One initial compile exposes the rejected operator lowering. One corrected
stable-family compile supplies all twelve maintained raster units. The strict
comparator checks every code byte, attached metadata and 141 explicit relocation
bindings. Thirty-three generated labels are renamed only after their actual
COFF section/value/type/storage/aux definitions agree; original targets and
addends remain unchanged. The twenty retired cleanup bindings are refreshed
without changing parent ownership or fragment counts.

| Complete entry | Original / rebuilt bytes | Differing bytes before / now |
| --- | ---: | ---: |
| Eight FixedPoint operations and horizontal span | 715 / 715 | 0 / 0 |
| Triangle `0x0040AB90` | 1710 / 1710 | 88 / 97 |
| Polygon `0x0040B550` | 1543 / 1543 | 216 / 216 |
| Clipped polygon `0x0040BB60` | 1592 / 1592 | 213 / 216 |

The nine exact functions retain 715 code bytes and 136 metadata bytes. Triangle
metadata remains exact across 160 bytes. The candidate increases are recorded,
not hidden by remapping: triangle changes nine raw bytes across three comparison
producers; clipped changes three in its unchanged positive dy/error comparison.
Independent review identifies these groups at rebuilt original-mapped addresses
`0x0040AC11`, `0x0040B001`, `0x0040B0B8` and `0x0040C134`. Their predicates remain
`y2 <= y3`, `y >= y3` twice, and `error < dy`, with the same destinations. The
comparison source statements, sizes and frame homes are unchanged. Full twelve-body byte identity
with the preceding source is **not** claimed. Continue recovery of real workspace,
edge and expression declarations from producers/consumers; these arithmetic
corrections do not resolve those declarations or justify layout/flag sweeps.

## Focused execution and retained acceptance

An O2 native library with UBSan compiles the real raster, host raster and
allocator owners plus a thin guarded caller. Six additions compare the original
operator against that real method: positive/negative boundary controls,
`INT_MAX+1`, `INT_MIN-1`, `-1+1` and `INT_MIN+INT_MIN`. The check observes the
original ADD, real by-value destruction, returned receiver, `RET 4`, restored
SEH, argument storage and guards.

Both polygon entries compare two finite contours: `[(0,0),(INT_MIN,1),(0,1)]`
and the same shape with `-1` replacing `INT_MIN`. The first reaches exactly the
negation boundary without a pixel span; the second performs one ordinary carry.
Complete guarded pixels, immutable points, allocation/free order, normalized
pointer arrays and scalar scratch agree. Original code and MulDiv IAT bytes
remain unchanged. The ordinary boundary contour is outside its general in-bounds
public contract; this one finite observation does not grant arbitrary out-of-bounds
polygon support. These triangle-shaped contours do not execute the triangle entry.

All ten new original/native comparisons pass without UBSan errors. Two separate
old-source subprocesses fail as expected: signed `INT_MAX+1` and negation of
`INT_MIN`. This demonstrates concrete language-level defects in the previous
source outside its earlier bounded scope, not an incorrect earlier acceptance.
No full-game execution or exceptional unwind is tested here.

The historical 7,164 raster vectors and 231 other affected semantic scopes are
not rerun. Their counts, scopes and oracle identities remain historical and
unchanged. Compatibility rests on unchanged arithmetic throughout their old
representable domain, complete compiler comparisons above, and the separate
boundary probes. Current source/header identities are refreshed in 235 input
inventories and the four direct raster rows, with the old ledger sealed in the
private receipt. No direct-case count or new semantic row is added.

Private `.analysis/raster-word-arithmetic-20261018/` retains compiler inputs,
both proposal objects, generated-label proof, complete comparisons, native build
identities, probe/control results, independent review and resource receipts.
A member-hash-verified archive retains disposable input/probe products before
their removal; the current canonical raster object and receipts remain available. The existing delivery
EXE remains the preceding fresh-build product; this checkpoint compiles the
changed owner but does not relink or claim a current full-game validation.
