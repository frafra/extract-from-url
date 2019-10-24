#!/usr/bin/env python3

from extract_from_url import extract_from_url

import argparse
import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download and extract files on-the-fly (ZIP files too)"
    )
    parser.add_argument("url", nargs="+")
    args = parser.parse_args()
    for url in args.url:
        progress_bar = tqdm.tqdm(unit="B", unit_scale=True)
        extract_from_url(url, progress_bar)
