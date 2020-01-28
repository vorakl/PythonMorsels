from operator import lt, gt

class float_range(object):

    def __init__(self, start, end=None, step=None):
        if end is None:
            self.end = start
            self.start = 0 if isinstance(start, int) else 0.0
        else:
            self.start = start
            self.end = end

        if step is None:
           self.step = 1 if isinstance(self.start, int) and \
                            isinstance(self.end, int) else 1.0
        else:
            self.step = step

        self.down = True if self.step < 0 else False
        
    def __iter__(self):
        return float_range_iter(self.start, self.end, self.step, self.down)

    def __reversed__(self):
        return float_range_reverse(self.start, self.step, len(self))

    def __len__(self):
        flen = (self.end - self.start)/self.step
        ilen = int(flen)
        if ilen < 0:
            return 0
        else:
            return ilen+1 if flen - ilen else ilen

    def __getitem__(self, index):
        length = len(self)
        if length == 0 or \
           index >= length or \
           (index < 0 and abs(index) > length ):
            raise IndexError('float_range object index out of range')
        elif index < 0:
            return self.start + (length+index)*self.step
        return self.start + index*self.step

    def __eq__(self, other):
        if not isinstance(other, (float_range, range)):
            return NotImplemented
        elif len(self) == 0 and len(other) == 0:
            return True
        else:
            return len(self) == len(other) and \
                   self[0] == other[0] and \
                   self[-1] == other[-1]

class float_range_iter(object):

    def __init__(self, start, end, step, down):
        self.curr, self.end, self.step, self.down = start, end, step, down
        self.cond = lt if not self.down else gt

    def __next__(self):
        if self.cond(self.curr, self.end):
            ret = self.curr
            self.curr += self.step
            return ret
        else:
            raise StopIteration

class float_range_reverse(object):

    def __init__(self, start, step, length):
        self.start, self.step, self.pos = start, step, length - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= 0:
            ret = self.start + self.pos*self.step
            self.pos -= 1
            return ret
        else:
            raise StopIteration

