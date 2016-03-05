from __future__ import absolute_import

# Use as:
#   @singleton
#   class Foo:
#       pass
# requires that __init__ take only self
def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


#
# Adapted from https://wiki.python.org/moin/PythonDecoratorLibrary#Cached_Properties
# Copyright 2011 Christopher Arndt, MIT License
#
class cached_property(object):
    '''Decorator for read-only properties evaluated only once.

    It can be used to created a cached property like this::

        # the class containing the property must be a new-style class
        class MyClass(object):

            @cached_property
            def randint(self):
                import random
                return random.randint(0, 100)

    The value is cached  in the '_cache' attribute of the object instance that
    has the property getter method wrapped by this decorator. The '_cache'
    attribute value is a dictionary which has a key for every property of the
    object which is wrapped by this decorator. Each entry in the cache is
    created only when the property is accessed for the first time.

    To manually clear a cached property value, do:

        del instance.property name

    Note this is similar but different from the cached_property decorator
    which is used in korper, as defined in e.g. body.chained.chained.cached_property

    '''
    def __init__(self, fget, doc=None):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__

    def __get__(self, instance, owner):
        # To avoid triggering run() in Breadboard, don't use getattr
        # until we know the attribute exists.
        instance.__dict__.setdefault('_cache', {})
        try:
            value = instance._cache[self.__name__] # FIXME pylint: disable=protected-access
        except KeyError:
            value = self.fget(instance)
            instance._cache[self.__name__] = value # FIXME pylint: disable=protected-access
        return value

    def __set__(self, instance, value):
        raise AttributeError("Cached properties are read only")

    def __delete__(self, inst):
        try:
            cache = inst._cache # FIXME pylint: disable=protected-access
            del cache[self.__name__]
        except (KeyError, AttributeError):
            pass
