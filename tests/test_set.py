import pytest
import random


@pytest.fixture()
def random_set1():
    print('entering')
    list = []
    for i in range(10):
        list.append(random.randint(-1000, 1000))
    yield set(list)
    print('exiting')


@pytest.fixture()
def random_set2():
    print('entering')
    list = []
    for i in range(10):
        list.append(random.randint(-1000, 1000))
    yield set(list)
    print('exiting')


def test1(random_set1):
    a = id(random_set1)
    random_set1.add(random.randint(-100, 100))
    b = id(random_set1)
    assert (a == b)


class TestClass:
    def test2(self, random_set1, random_set2):
        Set_union = random_set1.union(random_set2)
        for s in Set_union:
            assert (s in random_set1) or (s in random_set2)

    def test3(self, random_set1, random_set2):
        Set_intersection = random_set1.intersection(random_set2)
        for s in Set_intersection:
            assert (s in random_set1) and (s in random_set2)

    def test4(self, random_set1, random_set2):
        Set_difference = random_set1.difference(random_set2)
        for s in Set_difference:
            assert ((s in random_set1) and (s not in random_set2))


@pytest.mark.parametrize('i', list(range(10)))
def test5(i):
    with pytest.raises(TypeError):
        l = [i ** 2 for i in range(10)]
        Set = set(l)
        assert (Set[i] == l[i])
