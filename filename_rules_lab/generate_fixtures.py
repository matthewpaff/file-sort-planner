"""Construct original synthetic cases; not records of real filenames or past work."""
import argparse
import json

OPTIONS = [(".PDF", "documents"), (".png", "images"), (".MP3", "audio"),
           (".mp4", "video"), (".zip", "archives"), (".py", "code"), (".unknown", "other")]


def make_case(index):
    label = "synthetic-filename-{:04d}".format(index)
    kind = index % 13
    if kind == 0:
        return {"id": label, "input": ["../sample_{}.txt".format(index)], "expected_error": True}
    if kind == 1:
        return {"id": label, "input": ["Sample_{}.TXT".format(index), "sample_{}.txt".format(index)], "expected_error": True}
    if kind == 2:
        return {"id": label, "input": ["bad\nname_{}.txt".format(index)], "expected_error": True}
    if kind == 3:
        name, folder = ".local_{}".format(index), "hidden"
    elif kind == 4:
        name, folder = "README_{}".format(index), "other"
    else:
        extension, folder = OPTIONS[index % len(OPTIONS)]
        name = "sample_{}_café{}".format(index, extension)
    return {"id": label, "input": [name], "expected": [
        {"name": name, "folder": folder, "destination": folder + "/" + name}]}


def main():
    parser = argparse.ArgumentParser(description="Print synthetic cases as JSONL; does not modify Git history.")
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.count <= 10000:
        parser.error("Count must be between 1 and 10000")
    for index in range(args.count):
        print(json.dumps(make_case(index), ensure_ascii=True, sort_keys=True))


if __name__ == "__main__":
    main()
