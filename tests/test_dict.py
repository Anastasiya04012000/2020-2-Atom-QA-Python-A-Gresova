import pytest
import random


@pytest.fixture()
def random_dict(scope='class'):
    print('entering')
    yield {a: random.randint(-1000, 1000) for a in range(10)}
    print('exiting')


class TestClass:
    def test1(self, random_dict):
        a = id(random_dict)
        random_dict[0] = 1
        b = id(random_dict)
        assert a == b

    def test2(self, random_dict):
        assert (random_dict.get(1984) is None)

    def test3(self, random_dict):
        random_dict.clear()
        assert (random_dict == {})


def test4(random_dict):
    d1 = {a: a ** 2 for a in range(7)}
    d2 = {a: a ** 2 for a in range(7)}
    d = random_dict
    d1.update(d)
    for key in d1:
        if (key in d2) and (key in d):
            assert d1[key] == d[key]
        elif (key in d) and (key not in d2):
            assert d1[key] == d[key]
        elif (key in d2) and (key not in d):
            assert (d1[key] == d2[key])


@pytest.mark.parametrize('i', list([11, 15, 2]))
def test5(i):
    d = {a: a * 2 for a in range(10)}
    d[i] = i ** 5
    assert (i in d and d[i] == i ** 5)
