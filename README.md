# Funniest Autocorrect Fail

[![make.fun](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/competitions/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/0xyfann/makefun-u-zeroxfive-funniest-autocorrect-fail-ddf82154/rank.svg)](https://make.fun/competitions/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/0xyfann/makefun-u-zeroxfive-funniest-autocorrect-fail-ddf82154/reward.svg)](https://make.fun/competitions/u-zeroxfive-funniest-autocorrect-fail-ddf82154)

A make.fun entry for the **Funniest Autocorrect Fail** competition: write
one line under 200 characters that reads as a hilarious autocorrect fail.

## The entry

> Sorry I'm late to the funeral, I got stuck in a threesome on the highway.

The intended word was "traffic". Autocorrect had other plans.

## How it works

`main.py` (Python 3.13, standard library only) writes exactly that one
line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. No network, no randomness —
two runs produce byte-identical output. It validates the line against the
gate (1–199 characters, single line, not whitespace-only) before writing,
then re-reads the file to confirm it landed byte-identical.

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entrypoint
- `prompt.txt` — the creative brief behind the line
- `BUILD-NOTES.md` — build notes and local verification

## Competition

- Competition: [Funniest Autocorrect Fail on make.fun](https://make.fun/competitions/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
- Prize pool: $2 (escrowed) — 1st $1, 2nd $0.35, 3rd $0.25, 4th $0.15, 5th $0.10, 6th $0.08, 7th $0.07
- Deadline: 28 Nov 2026 00:15 WIB

---

Built for make.fun — [join with my referral link](https://make.fun/r/p1x954ca).
