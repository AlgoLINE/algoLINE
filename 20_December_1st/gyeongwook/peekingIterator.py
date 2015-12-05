class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.current = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.current

    def next(self):
        temp = self.current
        self.current = self.iter.next() if self.iter.hasNext() else None
        return temp

    def hasNext(self):
        return self.current is not None