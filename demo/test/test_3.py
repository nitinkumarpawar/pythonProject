import sys

import pytest

from demo.demo_project.sample_3 import add


@pytest.mark.skip
def test_add():
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python3.8")
def test_str():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "win32", reason="doesn't work on windows")
def test_add():
    assert add(1, 2) == 3
