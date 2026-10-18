#!/usr/bin/env python3
"""Generate public progress from ledgers, without copying original game assets."""
import csv
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("status", ROOT / "scripts/report-reconstruction-status.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    status = module.status()
    with (ROOT / "config/functions.csv").open() as stream:
        functions = list(csv.DictReader(stream))
    with (ROOT / "config/matches.csv").open() as stream:
        exact = {row["address"] for row in csv.DictReader(stream)}
    with (ROOT / "config/implemented.csv").open() as stream:
        source = {row["address"] for row in csv.DictReader(stream)}
    with (ROOT / "config/function-origins.csv").open() as stream:
        authored = {row["address"] for row in csv.DictReader(stream) if row["origin"] == "authored"}
    authored_source = len(authored & source)
    authored_exact = len(authored & exact)
    authored_remaining = len(authored - exact)
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="460" viewBox="0 0 900 460" role="img" aria-labelledby="title desc">',
           '<title id="title">DX-Ball reconstruction progress</title>',
           f'<desc id="desc">{status["source_present"]} source-present functions, {status["exact_functions"]} exact functions, out of {len(functions)} provisional candidates. Currently classified authored functions: {authored_source} source-present, {authored_exact} exact, {authored_remaining} awaiting exact matches.</desc>',
           '<rect width="900" height="460" rx="20" fill="#101722"/>',
           '<g font-family="sans-serif">',
           '<text x="34" y="46" fill="#eef4ff" font-size="25" font-weight="bold">DX-BALL  /  RECONSTRUCTION</text>',
           '<text x="34" y="75" fill="#9baec8" font-size="14">REA showcase · English v1.07 · Windows 95 · Ghidra + VC4.0</text>',
           f'<text x="34" y="109" fill="#4ed8b7" font-size="16">{status["exact_functions"]} exact functions · {status["exact_bytes"]} bytes</text>',
           f'<text x="470" y="109" fill="#f5bd57" font-size="16">{status["source_present"]} source-present · {status["semantic_validated_with_scope"]} scoped semantic</text>']
    for i, function in enumerate(functions):
        color = "#4ed8b7" if function["address"] in exact else "#f5bd57" if function["address"] in source else "#29384c"
        x, y = 34 + (i % 33) * 25, 132 + (i // 33) * 14
        svg.append(f'<rect x="{x}" y="{y}" width="22" height="10" rx="2" fill="{color}"/>')
    svg += ['<text x="34" y="388" fill="#9baec8" font-size="13">Green: exact compiler match · Amber: reconstructed source · Dark: remaining candidates</text>',
            '<text x="34" y="412" fill="#9baec8" font-size="13">Priority: recover authored functions, then verify full behavior of the VC4 build.</text>',
            f'<text x="34" y="436" fill="#9baec8" font-size="13">Classified authored: {authored_source} source-present · {authored_exact} exact · {authored_remaining} awaiting exact matches</text>',
            '</g></svg>']
    (ROOT / "resources").mkdir(exist_ok=True)
    (ROOT / "resources/progress.svg").write_text("\n".join(svg) + "\n")
    (ROOT / "docs/PROGRESS.md").write_text(
        "# Reconstruction progress\n\nRecover the authored functions as faithfully and exactly as possible first.\n"
        "Then rebuild with the original Visual C++ 4.0 compiler and validate the full game behavior.\n"
        "The current records cover gameplay, all five screen modes, resources, graphics and audio.\n\n"
        "| Fact | Count |\n| --- | ---: |\n"
        f"| Classified authored functions with source | {authored_source} |\n"
        f"| Classified authored byte-exact functions | {authored_exact} |\n"
        f"| Classified authored functions awaiting exact matches | {authored_remaining} |\n"
        f"| Provisional function candidates | {status['function_candidates']} |\n"
        f"| Parent-owned compiler fragments, counted separately | {status['parent_owned_compiler_fragments']} |\n"
        f"| Source-present functions | {status['source_present']} |\n"
        f"| Functions with scoped semantic acceptance | {status['semantic_validated_with_scope']} |\n"
        f"| Byte-exact functions | {status['exact_functions']} |\n"
        f"| Complete exact code bytes | {status['exact_bytes']} |\n"
        f"| Entries identified as runtime dependencies | {status['runtime_identified']} |\n"
        f"| Entries identified as compiler-generated code | {status['compiler_generated_identified']} |\n"
        f"| Origin still unclassified | {status['origin_unknown']} |\n\n"
        "The inventory includes game routines, runtime dependencies and compiler-generated code.\n"
        "The authored inventory remains provisional. Historical Wine campaigns provide bounded\n"
        "observations; full behavior of the restored VC4 game remains unverified.\n\n"
        "Continue with the [remaining authored matches](research/exact/REMAINING_EXACT_FUNCTIONS.md#authored-candidates).\n"
        "See [the architecture](ARCHITECTURE.md), [compiler matching](MATCHING.md),\n"
        "and [historical play observations](research/ORIGINAL_CAMPAIGN.md).\n\n"
        "Generated from the ledgers by `scripts/repo-python scripts/progress.py`.\n")
    print("generated resources/progress.svg and docs/PROGRESS.md")


if __name__ == "__main__":
    main()
