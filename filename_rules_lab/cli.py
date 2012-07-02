import argparse
import json
import sys

from .core import plan


def main(argv=None):
    parser = argparse.ArgumentParser(description="Preview folder rules for filenames. No file operations.")
    parser.add_argument("names", nargs="*")
    parser.add_argument("--check-fixtures", metavar="JSONL", help="Verify generated synthetic cases")
    args = parser.parse_args(argv)
    try:
        if args.check_fixtures:
            if args.names:
                parser.error("Use filenames or --check-fixtures, not both")
            from .fixture_check import check
            print("Verified {} synthetic fixtures.".format(check(args.check_fixtures, plan)))
        else:
            print(json.dumps(plan(args.names), indent=2, ensure_ascii=True))
        return 0
    except ValueError as error:
        print("error: " + str(error), file=sys.stderr)
        return 2
    except (OSError, UnicodeError) as error:
        print("error: " + str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
