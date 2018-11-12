#!/usr/bin/python3 

class I:
    import unittest
    from func_in_context import Context

class MyContext(I.Context):
    __all__ = ['func']

    def func(self):
        return 10

class ContextBad1(I.Context):

    def func(self):
        return 10

class Test_Context(I.unittest.TestCase):
    
    def test(self):
        with self.assertRaises(NameError):
            print(func())
        with MyContext(namespace=globals()) as c:
            self.assertEqual(func(), 10)
        with self.assertRaises(NameError):
            print(func())

    def test_bad(self):
        with self.assertRaises(AttributeError):
            with ContextBad1(namespace=globals()) as c:
                self.assertEqual(func(), 10)

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)
