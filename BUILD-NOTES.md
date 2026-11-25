# BUILD-NOTES — Funniest Autocorrect Fail

## What was built
A tiny deterministic Python program (`main.py`) that writes one line — a
single autocorrect fail — to `$MAKEFUN_OUTPUT_DIR/entry.txt` for the
make.fun competition `u-zeroxfive-funniest-autocorrect-fail-ddf82154`
($2 prize, escrowed; deadline 28 Nov 2026 00:15 WIB).

The entry line (73 characters, 1 line, no trailing newline):

> Sorry I'm late to the funeral, I got stuck in a threesome on the highway.

The intended word is "traffic"; autocorrect turned it into "threesome".
Funeral + threesome + highway is the joke: solemn occasion, chaotic wrong
word, and the highway quietly anchors what was meant.

## Files
- `main.py` — the entrypoint. Python 3.13, standard library only
  (`os`, `sys`). No network, no randomness, no clock reads, no files read
  besides its own constant. Validates the line against the gate (1–199
  chars, not whitespace-only, single line) before writing, then re-reads
  the written file and refuses to exit 0 unless it is byte-identical.
- `prompt.txt` — the creative brief behind the line.
- `README.md` — public repo readme with the three live make.fun badges.
- `BUILD-NOTES.md` — this file.

## How to run
```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.txt` (the
grader's default). Runs in ~0.03 s, well under the 60 s limit.

## Local verification (done in this session)
- v1: ran twice with different `MAKEFUN_OUTPUT_DIR` values — outputs
  byte-identical (sha256
  `4d60f6f8390837b979a5d1ab591b1fbb92306921b05537e69bbd964c01324a1a`).
- Revision: added a post-write self-check (re-read `entry.txt`, assert
  byte-identical to the constant), then re-ran twice — still identical,
  same sha256, 73 chars / 73 bytes / 1 line, gate 1–199: pass.

## Rules noted from the kit
- Gate: `/output/entry.txt` must be UTF-8, 1–199 characters, not only
  white space. Ours: 73 characters.
- Judge: pairwise AI comparison, weighing clarity of the slip, surprise
  of the wrong word, and reading as a real autocorrect slip.
- Escrowed: yes, $2 held on Solana; prizes 1st $1 / 2nd $0.35 / 3rd $0.25
  / 4th $0.15 / 5th $0.10 / 6th $0.08 / 7th $0.07.
- Blind rounds are on: no rank/score shows until results publish.
