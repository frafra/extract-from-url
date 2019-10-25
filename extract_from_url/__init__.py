import urllib.request
import libarchive  # libarchive-c
from pathlib import Path

__version__ = "0.2.0"

_mkdir = lambda path: Path(path).mkdir()
_open = open

def extract_from_url(url, progress_bar=None, mkdir_f=_mkdir, open_f=_open):
    request = urllib.request.urlopen(url)
    if progress_bar is not None:
        progress_bar.desc = filename = request.info().get_filename()
        progress_bar.total = int(request.headers.get("Content-length", 0))
    with libarchive.stream_reader(request.fp) as stream:
        for member in stream:
            if member.isdir:
                mkdir_f(member.path)
            elif member.isfile:
                fp = open_f(member.path, "wb")
                try:
                    for block in member.get_blocks():
                        fp.write(block)
                        if progress_bar is not None:
                            progress_bar.update(len(block))
                finally:
                    fp.close()
