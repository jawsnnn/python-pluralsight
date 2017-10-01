"""
The object of this code is to demonstrate that
adding a __call__ method in a class definition can
make that class's objects callable like methods.

In this instance, a class object declared like:

resolve = Resolver()

can be called like a method, i.e.

resolve('google.com')

AND, the _cache dict will retain entries between calls
in a session

"""


import socket

class Resolver:

    def __init__(self):
        self._cache={}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache
