"""
File: LazyList.py
Description: A generic wrapper for all sorts of generators. This is
because itertools doesn't return things that return true when yeeted
into isinstance(<itertools object>, types.GeneratorType). Also, maps,
ranges and other stuff that needs to be lazily evaluated.
"""

import types
import copy


class LazyList:
    def __call__(self, *args, **kwargs):
        return self

    def __contains__(self, lhs):
        if self.infinite:
            if len(self.generated):
                last = self.generated[-1]
            else:
                last = 0

            while last <= lhs:
                last = next(self)
                if last == lhs:
                    return 1
            return 0
        else:
            for temp in self:
                if temp == lhs:
                    return 1
            return 0

    def __getitem__(self, position):
        if isinstance(position, slice):
            start, stop, step = (
                position.start or 0,
                position.stop,
                position.step or 1,
            )
            if stop is None:

                @LazyList
                def infinite_index():
                    if len(self.generated):
                        for lhs in self.generated[position::step]:
                            yield lhs
                        temp = next(self)
                        while temp:
                            yield temp
                            temp = next(self)

                return infinite_index()
            else:
                ret = []
                for i in range(start, stop, step):
                    ret.append(self.__getitem__(i))
                return ret
        else:
            if position < 0:
                self.generated += list(self)
                return self.generated[position]
            elif position < len(self.generated):
                return self.generated[position]
            else:
                while len(self.generated) < position + 1:
                    try:
                        self.__next__()
                    except:
                        break
                return self.generated[position % len(self.generated)]

    def __init__(self, source, isinf=False):
        self.raw_object = source
        if isinstance(self.raw_object, types.FunctionType):
            self.raw_object = self.raw_object()
        elif not isinstance(self.raw_object, types.GeneratorType):
            self.raw_object = iter(self.raw_object)
        self.generated = []
        self.infinite = isinf

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.listify())

    def __next__(self):
        lhs = next(self.raw_object)
        self.generated.append(lhs)
        return lhs

    def __setitem__(self, position, value):
        if position >= len(self.generated):
            self.__getitem__(position)
        self.generated[position] = value

    def listify(self):
        temp = self.generated + list(self.raw_object)
        self.raw_object = iter(temp[::])
        self.generated = []
        return temp

    def output(self, end="\n"):
        print("⟨", end="")
        for lhs in self.generated[:-1]:
            print(lhs, end="|")
        if len(self.generated):
            print(self.generated[-1], end="")

        try:
            lhs = self.__next__()
            if len(self.generated) > 1:
                print("|", end="")
            while True:
                print(lhs, end="")
                lhs = self.__next__()
                print("|", end="")
        except:
            print("⟩", end=end)
