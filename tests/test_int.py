import random
import pytest


@pytest.fixture(scope='class')
def random_value1():
    print('entering')
    yield random.randint(-1000, 1000)
    print('exiting')


@pytest.fixture(scope='class')
def random_value2():
    print('entering')
    yield random.randint(-1000, 1000)
    print('exiting')


class TestClass:

    def test(self, random_value1, random_value2):
        assert type(random_value2 * random_value1) == int

    def test1(self, random_value1, random_value2):
        assert type(random_value1 + random_value2) == int

    def test2(self, random_value1, random_value2):
        a = random_value1
        id1 = id(a)
        a = random_value2
        id2 = id(2)
        assert id1 != id2


def test3(random_value1):
    print(random_value1)
    assert type(bin(random_value1)) == str


@pytest.mark.parametrize('i', list(range(3)))
def test4(i):
    with pytest.raises(TypeError):
        a = 5
        assert a[i] == 5
