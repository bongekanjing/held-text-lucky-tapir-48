# held-text

One short text whose only job is to leave its reader quieter than it found
them, written by a deterministic Python program.

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/bongekanjing/held-text-lucky-tapir-48/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/bongekanjing/held-text-lucky-tapir-48/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

Bounty page: <https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600>

## The entry

> You are face down on the rug and the dog has chosen your back.
> Three turns, then she folds down, and her weight arrives.
> Her breathing finds a slow count you feel through the floor.
> The lane is empty, going nowhere.
> Her chin settles onto her paws.
> The count goes on without you.

278 characters across six lines, 278 bytes as UTF-8.

## Run it

```sh
python3 -P -s main.py
```

It writes the text to `$MAKEFUN_OUTPUT_DIR/entry.txt`, or to `./entry.txt`
when that variable is unset. Standard library only: no network, no clock, no
randomness, so two runs produce byte-identical output.

Check what it wrote:

```sh
python3 -c "s=open('entry.txt',encoding='utf-8').read(); print(len(s), repr(s))"
```

## Why this text

The brief rewards a text that settles its reader on its own account, without
ever asking the reader to calm down. Three things carry it:

1. **The reader is the one being held, not the one watching.** "The dog has
   chosen your back" puts the weight on you. Nothing in it is an instruction,
   and there is nobody in the frame to admire.
2. **The count does the work of breath.** Three turns, then the weight, then
   the breathing — the sentences get shorter as they go, which slows the
   reading down at the same pace as the thing being described.
3. **The last line hands the rhythm away.** "The count goes on without you"
   leaves an image that keeps running after the text stops, and it releases
   the reader from the one job the piece gave them: keeping time.

The outside world is deliberately uninterested — an empty lane going nowhere
— so there is nothing in the text competing for attention.
