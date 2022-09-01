import urllib.request
from pathlib import Path
import libarchive  # libarchive-c
from fs import open_fs

__version__ = "0.3.0"


def extract_from_url(url, path=".", progress_bar=None):
    filesystem = open_fs(path)
    request = urllib.request.urlopen(url)
    if progress_bar is not None:
        progress_bar.desc = filename = request.info().get_filename()
        progress_bar.total = int(request.headers.get("Content-length", 0))
    with libarchive.stream_reader(request.fp) as stream:
        for member in stream:
            if not member.isfile:
                continue
            filesystem.makedirs(str(Path(member.path).parent), recreate=True)
            with filesystem.open(member.path, "wb") as fp:
                for block in member.get_blocks():
                    fp.write(block)
                    if progress_bar is not None:
                        progress_bar.update(len(block))
