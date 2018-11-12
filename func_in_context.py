#!/usr/bin/python3 

class I:
    import contextlib

class Context(I.contextlib.AbstractContextManager):
    __all__ = None #необходимо переопределить в подклассе

    def __init__(self, *, namespace):
        self.ns = namespace

    def __enter__(self):
        if self.__all__ is None:
            raise AttributeError('__all__ must be define in subclass')

        self.ns_old = self.ns.copy()
        self.ns.update({key: getattr(self, key) for key in self.__all__})
        return self

    def __exit__(self, *exp):
        self.ns.clear()
        self.ns.update(self.ns_old)

