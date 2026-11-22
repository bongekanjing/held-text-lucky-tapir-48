# held-text

One short text whose only job is to leave its reader quieter than it found
them, written by a deterministic Python program.

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/bongekanjing/held-text-lucky-tapir-48/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/bongekanjing/held-text-lucky-tapir-48/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

Bounty page: <https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600>

## The entry

> You are face down on the rug.
> The dog folds over your back.
> Three turns, then her weight.
> Her breathing counts slowly.
> Yours falls in behind it.
> The joists under the floor
> were trees once, and hold.
> The lane stays empty.
> Her chin comes down.
> Something in you
> stops keeping time.

278 characters across eleven lines, 278 bytes as UTF-8.

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
ever asking the reader to calm down. Four things carry it:

1. **The reader is the one being held, not the one watching.** "The dog folds
   over your back" puts the weight on you. There is nobody in the frame to
   admire, and nothing is asked of you.
2. **The breath is borrowed, not instructed.** "Yours falls in behind it"
   means the reader's own breathing is already slowing, which is different
   from being told to breathe. The lines run 29, 29, 29, 28, 25, 26, 26, 21,
   20, 16, 19 characters: the measure shortens as the piece goes, so the
   reading slows at the same rate as the thing described. That deceleration
   is the mechanism the judge names when it calls a text entraining.
3. **The floor is older than the dog.** "The joists under the floor were trees
   once, and hold" is the line that keeps working: the thing holding you up
   was a tree, and it held then, and it holds. That is a thought to return to.
4. **The close recontextualises instead of restating.** "Something in you stops
   keeping time" releases the reader from the only job the text gave them —
   counting — rather than summarising the scene.

The outside world is deliberately uninterested: an empty lane that will stay
empty. Nothing in the text competes with the weight on your back.
