# Filename Rules Lab

Preview extension-based destination folders for plain filenames. No files are read, renamed, or moved.

This original small project uses **Python 3.10+ and only its standard library**.
No packages, virtual environment, service, or network access are required.

## Run

From this repository directory:

```console
python filename_rules.py --help
python filename_rules.py notes.PDF photo.jpg script.py
python filename_rules.py --check-fixtures fixtures/cases.jsonl
python -m unittest discover -s tests -v
```

Extensions match without case sensitivity; dotfiles go to hidden, and unknown extensions go to other. Input order is preserved. Paths, control characters, and case-insensitive duplicate names are rejected. This is a planning exercise, not a cross-platform safe file mover.

Output is JSON (or a fixture-check summary). Exit codes are 0 for success,
1 for file failures, and 2 for invalid input. Errors go to stderr.
For file-based tools, `-` reads stdin. Use UTF-8 input files.

## Structure and branches

- `filename_rules_lab/core.py`: pure parsing or analysis logic.
- `filename_rules_lab/cli.py`: command arguments and file input/output.
- `filename_rules_lab/generate_fixtures.py`: deterministic original sample cases.
- `filename_rules_lab/fixture_check.py`: expected-result/error validation.
- `fixtures/cases.jsonl`: 367 synthetic cases, one added per artificial dated commit.
- `tests/`: independently chosen boundary cases plus corpus validation.

`feature/core` and `feature/cli` retain the corresponding development snapshots.
`data/synthetic-fixtures` marks the completed corpus; `docs/usage` and `main` contain
the final documentation and tests. There are no copied upstream commits.

## Generate examples

```console
python generate_fixtures.py --count 20
```

This prints reproducible JSONL and **does not create or date Git commits**. The
historical-looking Git timeline is a separate, documented simulation. Many cases
vary generated values; they do not imply separate design decisions or features.

Keep contributions focused, add a regression test for changed behavior, and run
the standard-library tests. Never add real private data or credentials. Record
actual dates for new work. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
