import access_codes

def test_case_1():
    assert access_codes.answer(["foo", "bar", "oof", "bar"]) ==  2

def test_case_2():
    assert access_codes.answer(["x", "y", "xy", "yy", "", "yx"]) == 5
