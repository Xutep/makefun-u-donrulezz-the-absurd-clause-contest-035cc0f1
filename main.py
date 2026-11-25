#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes a single original English sentence (146 characters) to
/output/entry.txt: a deadpan terms-of-service clause that reads like
real legal boilerplate until the absurdity hits. The joke is the
register as much as the words — a perpetual, royalty-free licence,
subletting, no notice — applied to something no one can license:
your own shadow.

Deterministic, standard library only, no network, no input files.
The output directory defaults to /output (the grading sandbox) and
may be overridden with the OUTPUT_DIR environment variable, which is
only used as a path.
"""

import os
from pathlib import Path

# One sentence, 146 characters: deadpan legal boilerplate that quietly
# turns absurd. The clause grants a perpetual, royalty-free licence to
# the reader's shadow, which the Company may then sublet.
CLAUSE = (
    "By using the Service, you grant the Company a perpetual, "
    "royalty-free license to your shadow, which may be sublet to "
    "third parties without notice."
)


def main() -> None:
    if not 1 <= len(CLAUSE) <= 200:
        raise ValueError(f"clause is {len(CLAUSE)} characters, must be 1-200")
    if CLAUSE.strip() != CLAUSE or not CLAUSE.strip():
        raise ValueError("clause must be non-blank text without padding")
    if CLAUSE.count(".") != 1 or not CLAUSE.endswith("."):
        raise ValueError("clause must be exactly one sentence")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(CLAUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
