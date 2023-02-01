from demo.demo_project.sample_1 import add


def test_add():
    assert add(1, 2) == 3


def test_str():
    assert add("a", "b") == "ab"
