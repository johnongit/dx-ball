# DirectSound dispatch correspondence

The resumed October 18 investigation maps all **49 register-relative sound
calls in 12 original functions** to their maintained typed source operations.
The [site ledger](SOUND_COM_SITES.csv) records every original call address,
receiver expression, vtable slot, argument expression and native REA Evidence
identity. This closes the sound portion of the source-site correspondence
question raised by the [declared-prefix audit](CRT_SUFFIX_OWNERSHIP.md#direct-transfers-in-the-declared-game-prefix).

## Whole-function authority

One unchanged canonical sound compilation compares all 17 complete owner units:
**4,756 exact code bytes, 235 actual relocation bindings and 12 full literal
references**. The literal references attest 845 bytes with multiplicity. The
complete initialization comparison includes its 70 Ghidra-body-excluded cleanup
jump bytes; the parsing comparison similarly retains its five-byte gap.
No new exact function is added.

The private report is `build/reports/sound-dispatch-20261018.json`, SHA-256
`5f5f0ccd3270d243deefbcf1195b52a5511563345ffea60a34eb7c5f868285d0`.
The canonical object is `build/exact/sound.obj`, SHA-256
`cbaecfd6be79c68101e17c5340a82c432cb38390741733660480fa9a18004d3b`.
The independent passive mapper reproduces those complete comparisons before
decoding relocated object instructions. It pairs source order and original call
order within each function, checks each vtable displacement, follows the
straight-line receiver/argument setup and requires the pushed `this` value to
equal the method receiver. Six absolute `MessageBoxA` import calls are excluded.

## Factory and buffer ownership

Initialization calls the existing six-byte import thunk at `0x416606`, whose
instruction is `JMP dword ptr [0x00441234]`. The verified PE import directory
names that cell `DSOUND.dll!DirectSoundCreate`. Initialization passes the output
address `0x421098`; the primary-buffer factory call passes output cell `0x42109C`.
These are static API output paths, conditional on the API's actual results.

The buffer helper at `0x4063A0` receives its device and output pointer as cdecl
arguments. Its observed incoming call at `0x405A7B` belongs to loader `0x405990`:
the caller passes the device loaded from `0x421098` and the current record
pointer from `0x4265D0 + 4*slot`. The record's buffer field is at offset zero,
so that pointer is also the buffer-output address. The helper invokes device
slot 3, byte offset `0x0C`, with its real 20-byte descriptor, output pointer
and null aggregation argument. This is the actual forwarded ownership boundary.

| Interface / receiver expression | Calls |
| --- | ---: |
| `IDirectSound`, device loaded from `0x421098` | 12 |
| `IDirectSound`, helper device argument | 1 |
| `IDirectSoundBuffer`, primary loaded from `0x42109C` | 8 |
| `IDirectSoundBuffer`, buffer at current sound-record offset zero | 28 |
| Total | 49 |

The three fresh global-xref results contain 53 sites for `0x421098`, 28 for
`0x42109C` and 88 for `0x4265D0`. They record Ghidra's exact-address reference
observations; they do not prove that no alias can write the corresponding state.

## Native corroboration and retained evidence

The successful memory-budget query supplies initialization dossier
`ev_69852d0b19513ed3d5e28004185b6253d8b407fbaf66d3b564653fcf40a8af8b`.
The resumed session reuses it and completes 15 additional requests, retaining
16 cumulative Evidence records and closing normally. Its elapsed time is
152.338 seconds under CPU35%, one CPU and the approved 1/2 GiB memory scope;
peak memory is 1,074,118,656 bytes, with 695 soft-high events and zero max/OOM
events. The Java heap remains 256 MiB. Earlier failed startup attempts remain
retained separately and are not counted as successful observations.

| Native question | Evidence ID |
| --- | --- |
| Buffer helper and observed caller | `ev_5062866bcb01ad7ba844a51c536c6cd45bbf045e521cac9ee209f1012b196531` |
| Loader and forwarded output | `ev_09b10b71c47b7d4494e499248834ca849389404b981e5ff07b6a17c58d51d233` |
| Import thunk | `ev_eee2aff2be32782c08c5eb51fb76ea1dd425902bd5f1356912afc46cd9507825` |
| Device-cell references | `ev_ab50f08f6e89315cb0be02124269a6c33ed5a4e9ea96e271f7a118bb60fd48d3` |
| Primary-cell references | `ev_00f1ee4547031fd74f86c6cf323bb194015421e65e2a90f6f46837dfa3c716bd` |
| Sound-table references | `ev_4e5506808eb52883ae229c56f9d6cd5430bec04b5cd7e5fa7ef5ed13cf248680` |

The native join checks all 49 call addresses and vtable offsets, 445 setup
instruction occurrences against original bytes and retained instruction sites,
and all 101 argument pushes. The CSV attaches the relevant original assembly
line and Evidence ID to each source site. Brackets in expressions mean 32-bit
memory reads; negative EBP displacements retain their unsigned 32-bit hex
representation. Argument arrays use callee order, with `this` first.

Raw records are in REA run
`2026-10-18T16-26-36.981Z-requests-2128383`; the cumulative snapshot is
`.analysis/rea/dxball.snapshot.json`. Private
`.analysis/rea/sound-dispatch-resumed-20261018/` retains requests, resource
receipts and `native-join.json`; the prior independent complete-object proof is
in `.analysis/sound-dispatch-20261018/`.
The closed proof, current snapshot, complete owner inputs and canonical object/
report are sealed in `.analysis/rea/completed-sound-dispatch-20261018.tar.gz`:
all 140 archive members verify by size and SHA-256, and all 29 protected inputs
retain their bytes, modes and timestamps. Twenty byte-identical result aliases
are removed after verification, releasing 10,264,576 allocated bytes. Current
tested products, the snapshot and immutable run records remain available.

These observations establish static COM roles and source correspondence.
Concrete live implementation addresses, object validity, call success, lifetime,
all-writers/no-alias claims and the final authored-function denominator remain
open. The other 128 source COM sites belong to DirectDraw families and remain
outside this correspondence proof. No game probe or full campaign follows.
