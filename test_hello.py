from hello import add, multi


def test_add():
    assert 2 == add(1, 1)

def test_multi():
    assert 6 == multi(2,3)



test_multi()