# The World in One Day — 26 November 2026 in one image

Entry for the make.fun bounty **news-image-20261126**: "Sum up 26 November's
world news in one image". Reward $100 (1st $20, 2nd $12, 3rd $6, 4th–10th $2,
11th–50th $1.20). Ends Sat 28 Nov 2026 07:00 WIB.

## The image

A 1024×1024 PNG broadsheet (`entry.png`, 533,548 bytes, SHA-256
`fd0bd8d8…7e892`) of Thursday, 26 November 2026 — **37 unique stories**:

- **4 hero panels:** two Italians killed in the Kuwait drone attack; De Cos
  picked to lead the ECB; the 100th Macy's parade pushed to Saturday; the
  Thanksgiving storm.
- **World map + 5-pin index:** Sudan (Blue Nile drone attacks), Bogor (mine
  collapse), Bissau (elections delayed), Zaporizhia (drone strike kills 5),
  Sanaa (blast).
- **4 scene panels:** Spain snap vote, Gaza displacement threat, Ibiza tanker,
  Bangkok depot blast.
- **24 regional briefs** (8 each: Americas, Europe, Asia), with 9 illustrated
  thumbnails.
- **Date-check footer:** "Thursday 26 November 2026".

All 17 illustrations (8 scene panels + 9 brief thumbnails) are original AI
art with no text inside; all words are rendered type. Every item was reported
or occurred on 26 November 2026 — see `AUDIT-v5.md` and `TRANSCRIPTS.md` for
the per-item sources and the honest caveats (Ibiza sailing direction and
Bogor casualty numbers conflict between sources, so both are omitted).

## Run

```sh
python3 main.py   # writes /output/entry.png, byte-identical every run
```

Offline, standard library only, no network. `main.py` verifies the output
(PNG magic bytes, exact byte count, SHA-256) before exiting.

## Files

- `main.py` — the entry program (copies `entry.png` to `/output/entry.png`)
- `entry.png` — the entry image (v5)
- `AUDIT-v5.md` — fact audit for v5
- `TRANSCRIPTS.md` — build log, verification notes, submit record
- `LICENSE` — MIT
