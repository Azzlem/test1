import pytest
from src.func_prog import open_file


def test_func_prog():
    assert type(open_file()) == list
