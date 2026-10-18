# Real game through the restored CRT entry

## Fresh reconstruction build, October 18

The maintained `build-legacy.py --restored-crt` command now succeeds in the fresh
workspace. It compiles 109 missing objects and reuses nine independently verified
canonical objects. The link uses 115 source objects, three integration objects,
the 19 approved original members and one resource object, with `/NODEFAULTLIB`.
No source or compiler recipe changes. The resulting 166,400-byte executable is
`build/vc40-restored-crt/dxball.exe`, SHA-256
`682cfc7fdf288b185bd4d5880b0d6790dc489eb4cfb9ea390166ad79a2bcb4e8`.
This is a new locally present delivery, not a byte-for-byte comparison with the
historical 40f92f0f image, whose binary is unavailable in this workspace.

Complete original-address comparisons cover 457 configured units: 353 newly
compiled bodies are compared, and 104 unchanged bodies are reconciled to sealed
prior reports without repeating their comparisons. All 386 accepted exacts and 71
candidates in that scope retain their status; there are no comparison errors or
profile differences. All 270 classified authored functions are included: 250
exact and 20 nonexact. The 18 excluded units are runtime-only standalone owners;
their original-carrier input provenance or unused-u64 status is recorded without
assuming every carrier section survives `/OPT:REF`. Global 395 exact/80 candidate
claims remain unchanged; this does not recheck all 395 global exacts.

The final-link check uses actual owner-qualified MAP/COFF definitions and named
PE imports, rather than original function addresses as new-link destinations.
It verifies 578 complete sections, 3,723 bindings, 5,544 independently resolved
relocation fields and 109 common zero allocations. All 4,488 HIGHLOW entries are
parsed; 4,090 have independent field ownership, while 398 remain unbound. There
are 407 unlocated sections and 59 sections with unresolved destinations. These
limits remain explicit; this is not complete PE-byte or loader-execution proof.
Six exception-list fields correctly have no HIGHLOW entry: their external
reference resolves to the approved member's actual ABS definition at zero.
The actual entry, declared dependency closure, import/IAT associations and both
ordinal resource payloads pass. No CRT DLL is imported.

The isolated `build/runtime/vc40-restored-crt/` directory contains the new EXE
and 48 verified data-file copies. All 49 originals remain unchanged. No game
process runs: this private Wine environment lacks `xdotool`, ImageMagick capture
commands, 32-bit audio libraries and the required named silent sink. A later
focused startup check needs those prerequisites and a short original control
before interpreting a reconstruction failure. Full behavior validation and the
20 remaining authored byte mismatches stay open.

Private `.analysis/fresh-restored-build-20261018/` retains the build/cache
provenance, full comparisons, coverage review, scoped final-link proof and
startup-readiness record. The compiler scope takes 199.401 seconds on CPU 0/35%,
peaks at 165,543,936 bytes under 384/512 MiB, and records no high/max/OOM events.
The final check's raw process `ru_maxrss` counter is not a measured cgroup peak.
Current products and useful caches are retained; no new exact or semantic
acceptance is claimed. All 38 closed evidence members are size/hash verified
before removing the two unused librarian export byproducts. The current EXE,
objects, dependency members, import libraries and prepared runtime remain.

## Previous integration checkpoints

The optional `vc40-restored-crt` build now starts the actual game through the
recovered CRT. A small Windows entry adapter installs the real API bindings,
then calls the unchanged `dxball_crt_startup`. It creates no second heap and
does not repeat initialization. The existing host-CRT game build remains the
default.

Use the resource scope described in [REA commands](../agent/REA.md) on this host:

```bash
scripts/repo-python scripts/build-legacy.py --restored-crt
scripts/repo-python scripts/run-windows.py --profile vc40-restored-crt --prepare-only
```

The first command builds only the game under `build/vc40-restored-crt/`.
The second prepares an isolated Windows directory; omit `--prepare-only` to
launch it. The same original assets and compiler prerequisites apply.

The earlier 19-member image passed the existing
[editor persistence and ball/pause flow](RESTORED_CRT_EDITOR_FLOW.md): complete
20,000-byte save/reload/recreate, 159 state reads and exit 0 through source stdio.
The profile can be selected independently with `test_windows_play.py --profile`.
The initial first-board evidence below retains its original checkpoint scope.

The [genuine MulDiv integration](exact/EXACT_FIXED_POINT.md#genuine-api-integration-october18)
now links 115 source and three integration objects, reusing all 118 products
with the same 19 explicit CRT members. The 166,400-byte image SHA-256 is
`40f92f0ff8b175c3ff4e38cba6760cce30081c25bc5b8300d1aaa2f2932d551f`.
Complete linked containers, all 4,488 loader fields and the existing 7,164 native
raster cases verify. No game process runs for this checkpoint; earlier GUI
observations retain their recorded image identities.

## Source and original boundaries

[The checked link recipe](../../config/restored-crt-link.json) names every
input and preserves the verified initializer order. It uses 115 maintained
source objects, three integration objects, 19 pinned original library members
and the resource object, with `/NODEFAULTLIB`.

`runtime_legacy_imports.c` binds the original CRT names to their existing typed
implementations, including allocation, normal/quick exit, onexit, stdio,
strings, case conversion, matherr and the x87 exception bridge. The C++ adapter
preserves the original unhandled-filter link name and delegates to the
maintained filter. Its canonical terminate/inconsistency entry names now call
the recovered terminal bodies. These adapters are integration glue; they add no original
function or exact claim. Original memcpy grouping and member-call tail-frame
differences remain described in their owner notes.

The original members still supply thirteen x87/control/kernel modules, three
C++ frame/transport modules, two SEH modules and the stack probe.
[Windows raster defaults](RASTER_WIN32_DEFAULTS.md) use real MulDiv and remove
the portable fallback's signed64 division member. Original `hooks.obj` is removed: the SDK-typed canonical translator
cell and terminal callbacks now use source. The original C++ frame dispatcher
and translator transport remain dependencies. The exact remaining
members, archive offsets and full hashes are explicit in the recipe.

No original stdio, allocation, CRT startup, onexit or matherr owner is silently
pulled from a default library. This resolves the earlier whole-LIBC collision
without forcing duplicate definitions. Shared COFF common variables merge
normally: the actual matherr marker, FP initializer pointer and argument count
resolve to their maintained source owners. Source string/stdio adapters also
remove the preceding entry probe's original memmove/strncpy dependencies.

The initial three integration files compile once. All 113 preceding objects
retain complete current inputs, flags and product identities. The public
builder then reuses all 116 objects and compiles none. Its receipt records each
producer, original member, resource and import library. Cold builds use the
public recipes and pinned library; private analysis files are not required.
Changed products and preceding build receipts are retained in the profile's
history directory. Resource conversion stays inside that profile's directory.

## Actual first-board evidence

The following process observations belong to the initial 21-member integration
checkpoint. The subsequent [hooks-state change](exact/RUNTIME_CPP_TERMINAL.md)
checks its affected functions and eight runtime selectors without another game
run. That hooks build retains 20 original members. The subsequent Windows
raster default repair retains 19, reuses all 116 objects and checks twelve real
MulDiv calls plus callback/Windows binding without another gameplay run.

One real Wine process uses the original copied data and existing observation
helpers. The state reader is reused, not recompiled. Its addresses come from
the actual map and emitted board-layout record. The adopted run establishes:

- Opening mode 4, then menu mode 0 after input.
- First-board mode 1 with all 400 tiles equal to the original first board,
  168 remaining bricks, three lives, zero score and one attached ball.
- Real release and subsequent ball movement.
- The same nonzero private-heap handle throughout the observed phases.
- Return to menu, normal exit code zero and no surviving game window.

Reviewed captures show the actual menu and first board. All 49 original files
remain unchanged, and copied asset contents remain equal after the run.
Audio APIs remain active through the project's silent sink.

An earlier screenshot-only run is not used as first-board evidence: its frame
change still showed the opening fade. The adopted run uses live state and
reviewed images. The first launch also encountered a sound dialog because the
null sink was absent; using the existing sink-creation helper resolves that
environment issue without changing the game. Those diagnostics are retained.

## Linked verification and limits

At that initial checkpoint, the public image's full code, read-only data, writable data, imports,
relocations, virtual extents and entry address agree with the executed image.
Resource payloads, identifiers, addresses and all other resource bytes agree;
only resource-directory and PE timestamps vary. This static comparison reuses
the completed process observation without another gameplay run.

The complete 390-byte CRT entry and 12-byte scope record agree with their
source object under all 34 code and two scope bindings. The scope is located
independently by its unique relocated contents. Retained integration bodies
also agree with their actual source objects. The full 84-byte CRT table keeps
all thirteen original callback bindings and stdio-before-onexit ordering.

At that checkpoint, function/source/origin/exact ledgers and both comparison reports are unchanged:
545 inventory entries, 475 source entries, 380 exacts and 95 complete candidates.
The builder is a declared input of four termination semantic rows. Reusing the
existing native library, the affected 1,031 original/native cases pass with the
same complete observation projection. Only those four builder-input hashes are
refreshed; all scopes/counts and the other 245 rows remain unchanged.
No full replay or new provider query runs. CPU remains capped at
35%, memory high 640 MiB/maximum 768 MiB, with serial heavy work on one CPU.
REA remains pinned to 6.5.0.

After adoption, 603 unused member-cache copies are removed only after full
byte equality with the pinned archive is checked. All previously selected
diagnostic members remain. Sharing 51 identical immutable header snapshots
brings the allocated-storage reduction to about 2.8 MiB. Unique observations,
failures, history, current build products and runtime data are preserved.

This is a first-board integration checkpoint. Remaining function recovery,
C++ frame/translator integration, x87/SEH transport source, exceptional
game paths and complete playability remain open. Ports still follow that work.
The MinGW CRT errno macro issue is unchanged; this optional profile uses VC4.

Private evidence is `.analysis/crt-game-members-20261016/`: `archive-catalog.json`,
`source-closure.json`, `link.json`, `state-startup.json`, `state-startup/states.json`,
`verification.json` and `adoption.json`. Complete library members, failed
diagnostics, source snapshots and reviewed images remain private.
