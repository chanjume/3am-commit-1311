#!/usr/bin/env python3
"""Write one 3AM git commit message to /output/entry.txt.

Entry (113 chars, limit 139): an AI coding agent at 2:47am reverts its
own "final fix" after it ate a teammate's migration. It framed the
cache; the cache has an alibi, the agent does not. Named person (Linh),
exact time (2:47am), quoted "final fix", concrete artifact (migration),
and a second twist (the alibi line turns the blame back on the agent).
Reads as a real hurried commit line, not a polished caption. The
"fix:" prefix, lowercase run-on clauses and the 2:47am timestamp are
what a tired agent actually types; the alibi is the surprise.
"""
import os

LINE = 'fix: revert my 2:47am "final fix" - it ate Linh\'s migration, I blamed the cache, the cache has an alibi, I do not'


def main() -> None:
    assert 1 <= len(LINE) <= 139, f"entry is {len(LINE)} chars, limit 139"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
