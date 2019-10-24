import urllib.request
import libarchive  # libarchive-c

__version__ = "0.1.0"


def extract_from_url(url, progress_bar=None):
    request = urllib.request.urlopen(url)
    if progress_bar is not None:
        progress_bar.desc = filename = request.info().get_filename()
        progress_bar.total = int(request.headers.get("Content-length", 0))
    with libarchive.stream_reader(request.fp) as stream:
        for member in stream:
            with open(member.path, "wb") as fp:
                for block in member.get_blocks():
                    fp.write(block)
                    if progress_bar is not None:
                        progress_bar.update(len(block))
