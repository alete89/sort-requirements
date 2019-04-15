import os

from sort_requirements import sort_requirements


FIXTURES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fixtures")


class TestSortRequirements(object):
    def test_simple_file(self):
        with open(os.path.join(FIXTURES_DIR, "simple.txt"), "r") as f:
            txt = f.read()
        with open(os.path.join(FIXTURES_DIR, "simple-sorted.txt"), "r") as f:
            expected = f.read()
        txt = sort_requirements(txt)
        assert txt == expected

    def test_hashes_file(self):
        with open(os.path.join(FIXTURES_DIR, "hashes.txt"), "r") as f:
            txt = f.read()
        with open(os.path.join(FIXTURES_DIR, "hashes-sorted.txt"), "r") as f:
            expected = f.read()
        txt = sort_requirements(txt)
        assert txt == expected

    def test_complex_file(self):
        with open(os.path.join(FIXTURES_DIR, "complex.txt"), "r") as f:
            txt = f.read()
        with open(os.path.join(FIXTURES_DIR, "complex-sorted.txt"), "r") as f:
            expected = f.read()
        txt = sort_requirements(txt)
        assert txt == expected
