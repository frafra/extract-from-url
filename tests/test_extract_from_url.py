from extract_from_url import extract_from_url


def test_targz():
    try:
        extract_from_url(
            "https://files.pythonhosted.org/packages/93/c4/d8fa5dfcfef8aa3144ce4cfe4a87a7428b9f78989d65e9b4aa0f0beda5a8/libarchive-c-4.0.tar.gz",
            "temp://extract-from-url_test",
        )
    except Exception as exc:
        assert False, exc
