import unittest
from class_to_test import MethodsToTest


class TestMethods(unittest.TestCase):
    def test_method1(self):
        obj = MethodsToTest()
        self.assertTrue(obj.method1())

    def test_method2(self):
        obj = MethodsToTest()
        self.assertFalse(obj.method2())

    def test_method3(self):
        obj = MethodsToTest()
        self.assertTrue('Bla', obj.method3())

    def test_method4(self):
        obj = MethodsToTest()
        self.assertTrue(TypeError, obj.method4(), 'c')
