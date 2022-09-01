#!/usr/bin/env python3

from extract_from_url import extract_from_url

import argparse
try:
    import tqdm
except ImportError:
    progress_bar = None
else:
    progress_bar = tqdm.tqdm(unit="B", unit_scale=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download and extract files on-the-fly (ZIP files too)"
    )
    parser.add_argument(
        "--dest",
        default=".",
        help="location where files will be saved (supports PyFilesystem FS URLs)",
    )
    parser.add_argument("url")
    args = parser.parse_args()
    extract_from_url(args.url, args.dest, progress_bar)
