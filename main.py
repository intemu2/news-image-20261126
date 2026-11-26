"""World news of 26 November 2026 in one image — make.fun news-image-20261126.

Entry for Firt / intemu2. A 1024x1024 PNG broadsheet: 4 hero scene
panels (two Italians killed in the Kuwait drone attack; De Cos picked
to lead the ECB; the 100th Macy's parade pushed to Saturday; the
Thanksgiving storm), a labelled world map with a 5-pin index (Sudan,
Bogor, Bissau, Zaporizhia, Sanaa), 4 more scene panels (Spain snap
vote, Gaza displacement threat, Ibiza tanker, Bangkok depot blast),
24 regional briefs (8 each for the Americas, Europe and Asia) and a
date-check footer. 37 unique stories, no story repeated; every item
was reported or occurred on Thursday, 26 November 2026. Sources:
Daily Summary Of, OneTurn, Reuters, AFP and dated digests (see
TRANSCRIPTS.md for the honest two-tier verification and the
Ibiza-direction / Bogor-numbers caveats).

The image is the entry's own artwork, built in-session by the agent's
build script (see TRANSCRIPTS.md for the five-version build log); this
program is deliberately offline and dependency-free: it only copies
the entry's image file beside it to /output/entry.png. Standard
library only, no network.
"""

import hashlib
from pathlib import Path

EXPECTED_SHA256 = "fd0bd8d852e8e4c2e6ae20429d67aea6fd6d763ff17ab329926cf78894d7e892"
EXPECTED_BYTES = 533548

SOURCE_PATH = Path(__file__).resolve().parent / "entry.png"
OUTPUT_PATH = Path("/output/entry.png")


def main() -> None:
    data = SOURCE_PATH.read_bytes()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(data)
    # Read back and prove the gate before exiting: PNG magic bytes, exact
    # byte count, and SHA-256 must match the audited v5 image. If the file
    # ever holds anything else, fail loudly instead of shipping it.
    written = OUTPUT_PATH.read_bytes()
    if written[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png must start with the PNG magic bytes")
    if len(written) != EXPECTED_BYTES:
        raise ValueError(f"entry.png must be {EXPECTED_BYTES} bytes, got {len(written)}")
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"entry.png SHA-256 mismatch: {digest}")
    print(f"wrote {OUTPUT_PATH} ({len(written)} bytes, sha256 {digest[:12]}...)")


if __name__ == "__main__":
    main()
