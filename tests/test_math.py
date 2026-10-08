from ai_engineering_git_lab import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_number():
    assert add(-2, 3) == 1


def test_subtract():
    assert subtract(5, 2) == 3





