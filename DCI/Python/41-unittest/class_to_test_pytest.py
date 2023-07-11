import pytest
from class_to_test import MethodsToTest

obj = MethodsToTest()


@pytest.mark.skip('Do not run')
def test_method():
    assert obj.method1()


@pytest.mark.skipif(True, reason='also skipped')
def test_mothod2():
    assert not obj.method2()


@pytest.mark.Test3
def test_method3():
    assert obj.method3() == 'Bla'


def test_method4():
    with pytest.raises(KeyError):
        obj.method4('c')


def test_method5():
    with pytest.raises(TypeError):
        obj.method5()


@pytest.mark.parametrize('input, expected', [(1, 1), (2, 2)])
def test_method6(input, expected):
    assert input == expected
