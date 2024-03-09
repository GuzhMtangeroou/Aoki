# coding: utf-8

# MIT License
#
# Copyright (c) 2024 BigCookie233
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import inspect

event_listeners = {}


class Event:
    def call(self):
        if self.__class__ in event_listeners:
            for listener in event_listeners[self.__class__]:
                listener(self)


def event_listener(*args, **kwargs):
    if args[0] is None:
        raise TypeError("missing 1 required argument")
    if not issubclass(args[0], Event):
        raise TypeError("incorrect argument")

    def wrapper(func):
        if len(inspect.signature(func).parameters) != 1:
            raise TypeError("The listener takes 0 positional arguments but 1 will be given")
        event_listeners.setdefault(args[0], []).append(func)

    return wrapper