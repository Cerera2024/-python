import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitilize(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("SkyPro") == "Skypro"
    assert string_utils.capitilize("123abc") == "123abc"
    assert string_utils.capitilize("") == ""

def test_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   sky pro   ") == "sky pro   "
    assert string_utils.trim("") == ""

def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("", ",") == []
    assert string_utils.to_list("single") == ["single"]

def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S") == True
    assert string_utils.contains("SkyPro", "U") == False
    assert string_utils.contains("", "a") == False
    assert string_utils.contains("SkyPro", "o") == True

def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"
    assert string_utils.delete_symbol("", "a") == ""

def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S") == True
    assert string_utils.starts_with("SkyPro", "P") == False
    assert string_utils.starts_with("", "a") == False
    assert string_utils.starts_with("SkyPro", "") == True

def test_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o") == True
    assert string_utils.end_with("SkyPro", "y") == False
    assert string_utils.end_with("", "a") == False
    assert string_utils.end_with("SkyPro", "") == True

def test_is_empty(string_utils):
    assert string_utils.is_empty("") == True
    assert string_utils.is_empty(" ") == True
    assert string_utils.is_empty("SkyPro") == False
    assert string_utils.is_empty("  SkyPro  ") == False

def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string([]) == ""

if __name__ == "__main__":
    pytest.main()
