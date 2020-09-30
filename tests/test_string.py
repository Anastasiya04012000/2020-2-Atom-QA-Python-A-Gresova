import pytest
import random
import string


@pytest.fixture()
def random_string1():
    print('entering')
    yield ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(7))
    print('exiting')


@pytest.fixture()
def random_string2():
    print('entering')
    yield ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(7))
    print('exiting')


@pytest.fixture()
def random_string3():
    print('entering')
    yield ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(7))
    print('exiting')


def test1(random_string1):
    with pytest.raises(TypeError):
        random_string1[0] = "9"
        assert (random_string1[0] == "9")


class TestClass:
    def test2(self, random_string1):
        random_string1 = random_string1.upper()
        for w in random_string1:
            assert ((ord(w) >= 65) and (ord(w) <= 90)) or ((ord(w) >= 192) and (ord(w) <= 223))

    def test3(self, random_string1, random_string2):
        s = random_string1 + random_string2
        for i in range(len(random_string1)):
            assert (random_string1[i] == s[i])
        for i in range(len(random_string2)):
            assert (random_string2[i] == s[i + len(random_string1)])


def test4(random_string1, random_string2, random_string3):
    s = random_string1 + random_string2
    a = s.index(random_string1)
    assert (a == 0)
    b = s.index(random_string2)
    assert (b == len(random_string1))
    with pytest.raises(ValueError):
        c = s.index(random_string3)
        assert (b == len(random_string1) + len(random_string2))


@pytest.mark.parametrize('i', [random.choice(string.ascii_uppercase + string.ascii_lowercase),
                               random.choice(string.ascii_uppercase + string.ascii_lowercase),
                               random.choice(string.ascii_uppercase + string.ascii_lowercase)])
def test5(i, random_string1):
    sum = 0
    res = random_string1.count(i)
    for c in random_string1:
        if c == i:
            sum += 1
    assert (sum == res)
