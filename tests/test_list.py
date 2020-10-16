import pytest
import random


@pytest.fixture()
def random_list1(scope='session'):
    print('entering')
    list = []
    for i in range(10):
        list.append(random.randint(-1000, 1000))
    yield list
    print('exiting')


@pytest.fixture(scope='session')
def random_list2():
    print('entering')
    list = []
    for i in range(10):
        list.append(random.randint(-1000, 1000))
    yield list
    print('exiting')


class TestClass:
    def test1(self, random_list1):
        print(random_list1)
        a = id(random_list1)
        b = id(random_list1)
        assert (a == b)

    def test2(self, random_list1):
        random_list1.sort()
        for i in range(1, len(random_list1)):
            assert (random_list1[i] >= random_list1[i - 1])

    def test3(self, random_list1):
        list = random_list1.copy()
        assert (list == random_list1)
        assert (id(list) != id(random_list1))


def test4(random_list1, random_list2):
    a = random_list1
    b = random_list2
    len1 = len(a)
    len2 = len(b)
    a.extend(b)
    assert (len1 + len(b)) == len(a)


@pytest.mark.parametrize('i', list([0, 1, 3, -1, 100, 0.9]))
def test5(i):
    list1 = [1, 2, 3, 4, 5, 6, 7]
    if i >= 0 and type(i) == int:
        assert len(i * list1) == i * len(list1)
    elif i < 0 and type(i) == int:
        with pytest.raises(AssertionError):
            assert len(i * list1) == i * len(list1)
    else:
        with pytest.raises(TypeError):
            assert len(i * list1) == i * len(list1)
