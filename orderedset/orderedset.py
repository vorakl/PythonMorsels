from collections.abc import Iterable

class OrderedSet(object):
    def __init__(self, iterable):
        self.oset = dict()
        self.add(iterable)

    def add(self, items):
        if isinstance(items, Iterable):
            for item in items:
                if item not in self.oset:
                    self.oset[item]=len(self.oset)
        else:
            if items not in self.oset:
                self.oset[items]=len(self.oset)

    def discard(self, item):
        try:
            self.oset.pop(item)
        except KeyError:
            pass

    def __iter__(self):
        return iter(sorted(self.oset.keys(), key=lambda x: self.oset[x]))

    def __len__(self):
        return len(self.oset)

    def __contains__(self, item):
        return item in self.oset

    def __eq__(self, value):
        if isinstance(value, OrderedSet):
            for item1, item2 in zip(self, value):
                if not item1 == item2:
                    return False
            return len(self) == len(value)
        elif isinstance(value, set):
            for item in self:
                if item not in value:
                    return False
            return len(self) == len(value)
        else:
            return False

    def __getitem__(self, key):
        return sorted(self.oset.keys(), key=lambda x: self.oset[x])[key]
