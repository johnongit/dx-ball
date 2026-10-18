# Rotation displacement and text-width words

October 18, 2026. Two shared implementations now preserve original 32-bit
arithmetic at previously unproved boundaries. Rotation extends its row displacement
with the original sign on a 64-bit host; measurement accumulates widths modulo
32 bits before returning the signed result. These are source-fidelity corrections,
not new authored functions, exact promotions or a full-game validation.

## Rotation source-row displacement

The complete saved REA 6.5.0 listing has 365 instructions through `0x00402CC3`:
`ev_5c4373e9df5331a897168e1c26b16eafd66ba33d289e16dcd4dfa14324288d6c`.
At `0x00402C12` it loads the signed descriptor pitch, subtracts the captured
unsigned width, increments the word and adds it to the 32-bit source cursor
at `0x00402C1F`. No new import or provider query is needed for this sequence.

Previously `pixel += source_desc.pitch - width + 1` computed an unsigned
32-bit delta, then zero-extended it for native pointer arithmetic. For width 2
and pitch −4, the intended −5 became +4,294,967,291 on the 64-bit host. The
source now casts the completed word to `DxBallInt` before pointer addition.
It retains the original unsigned subtraction and increment, avoiding a newly
introduced signed subtraction overflow. VC4 emits identical complete code.

Four finite views compare source pitch ±4 and destination pitch ±35 independently.
Each uses a 2×3 sprite, angle 0 and center (16,12). Source backing includes the
final formed cursor after the last pixel, even though it is not dereferenced.
Complete source/destination allocations, padding and guards, bank/record state,
trig tables, six source-pixel positions and all three ADD32 row rollovers agree
between the original and the corrected real native method. GetSurfaceDesc,
Lock and Unlock preserve their ordered controlled calls. The normal floating
runtime branch and the real original/native trig initialization execute.

The old native library passes the positive-pitch control. Its negative-source
control runs only in an isolated child, with core files disabled and a time
bound. Before entry it verifies that the predicted erroneous second-row address
is unmapped; the child then terminates with SIGSEGV. The corrected library
passes that same geometry. This is a controlled typed surface boundary;
physical DirectDraw driver availability of negative pitches is not established.
The claim remains bounded by valid backing, signed representable displacement
and coordinate products, finite geometry and eventual lock success.

## Measurement accumulation

The fresh complete 279-byte REA listing has 79 instructions through `0x004050E6`:
`ev_982bc518236d3b9e8028b376bc8c31b84758afae4b2d4cfac4d6a278a11280c0`.
Fallback uses signed division by two, then DWORD ADD at `0x004050A5`; a hit adds
spacing at `0x004050CC` and accumulates at `0x004050D2`. No overflow flag is
consumed, and the result word returns in EAX. Incoming-reference Evidence
`ev_3431ec9deba01d0da0f20e38e7603f7d490db10a3229f17c5ef5b25455b4ec3e`
identifies external sites in centered text, intro and high-score drawing;
its other entries are internal branches, not additional callers.

The implementation keeps signed indices and a 32-bit unsigned accumulator.
The hit-path glyph width converts to unsigned before adding spacing, defining
both additions modulo 2^32. The missing-glyph half-width remains signed before
accumulation, preserving its truncation toward zero. An explicit signed return
conversion retains the supported targets' two's-complement result mapping.
This follows observed word behavior without asserting the original local's
historical type or spelling; the previous representable-domain scope was valid.

Five finite cases use one initialized glyph record and at most three text
bytes: safe hit, inner hit overflow, outer accumulation overflow, safe fallback
and fallback overflow. The original read guard permits only initialized fields
and text; it observes all ADD sites and rejects nonstack writes. Complete
bank/record/text storage, guards, selection, spacing, return and cdecl stack
state agree. Three old-source child processes fail UBSan on their respective
signed overflows; all corrected cases pass. No physical surface with these
extreme dimensions is created, and no drawing or gameplay reachability is claimed.

## Build and complete comparison

One serial VC4 compile per stable owner supplies all twelve UI/rotation units.
All complete raw and relocation-resolved code identities stay unchanged:

| Family | Complete units | Exact functions / code bytes |
| --- | ---: | ---: |
| Rotation | 5 | 4 / 900 |
| UI/text | 7 | 6 / 896 |

All 153 actual bindings and 25 complete-literal references compare. Four bound
compiler literal symbols change ordinal across 19 sites. Their actual definitions
and complete 40-byte readonly container agree; original targets/addends remain
unchanged. No metadata or same-section binding is omitted. Independent read-only
comparison reproduces all twelve results and the full COFF audit finds only
literal-symbol names and object timestamps changed.

The remaining complete candidates are unchanged: renderer `0x004026A0` emits
1458/1572 bytes with 1466 differing positions, and measurement `0x00404FD0`
emits 279/279 with three. Continue real renderer workspace/frame recovery and
the original text outer-comparison declaration context. These boundary fixes
do not justify spelling, flag, layout or name sweeps.

Two focused native libraries use actual resources, rotation, UI, trig and
allocator/host bodies, with three typed fixture data definitions for otherwise
external state. No function body is replaced. They use O2+UBSan; C++ vptr checking
is excluded because the controlled C vtables supply no C++ RTTI. The first build
stops on the known ignored-fread warning before producing an object; the retry
permits only unused-result warnings in resources.cpp, preserving its original
loader behavior. That loader is not executed here. This is not a full-core build.

All nine new original/native cases pass. Historical renderer/wrapper, text and
other owner matrices are not rerun: unchanged complete VC4 identities and source
algebra within their prior defined domains provide the explicit compatibility
chain. Ten exact receipts, eight direct semantic source identities and 235 input
inventories refresh; historical cases, scopes and oracle hashes remain fixed.
No exact/source count changes, delivery relink or game process follow.

Private `.analysis/word-width-recovery-20261018/` retains the full comparison,
literal proof, ledger chain and independent reviews. Companion
`.analysis/rotation-signed-pitch-20261018/` and
`.analysis/text-width-word-20261018/` retain frozen build/probe inputs, normal
and failure controls, and resource receipts. The closed archive verifies every
member before removing disposable copied inputs and native probe products.
Current canonical VC4 objects and useful caches remain.
