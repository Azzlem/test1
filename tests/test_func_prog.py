import pytest
from src.func_prog import open_file, fix_dict, change_, change_two


def test_func_prog():
    assert type(open_file()) == list


def test_func_prog_next():
    assert type(fix_dict()) == list


def test_func_prog_next_next():
    assert type(change_("Maestro 1596837868705199")) == str
    assert change_(None) == ""
    assert change_("Maestro 1596837868705199") == "Maestro"
    assert change_("Visa Classic 6831982476737658") == "Visa Classic"


def test_func_prog_next_next_next():
    assert change_two("Счет 35383033474447895560") == "3538 30** **** 47895560"
    assert change_two(None) == ""
    assert change_two("Visa Classic 6831982476737658") == '6831 98** **** 7658'

