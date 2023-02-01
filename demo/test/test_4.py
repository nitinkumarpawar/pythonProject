import sys

import pytest

from demo.demo_project.sample_4 import add


@pytest.mark.skip
def test_add():
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python3.8")
def test_str():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "win32", reason="doesn't work on windows")
def test_add():
    assert add(1, 2) == 3


@pytest.mark.parametrize("a,b,c", [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
def test_add(a, b, c):
    assert add(a, b) == c
