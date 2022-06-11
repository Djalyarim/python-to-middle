import os
from contextlib import contextmanager


@contextmanager
class TempFile:

    def __init__(self, path) -> None:
        super().__init__()
        self.path = 'file.tmp'
        self._f = open(path, 'wb')

    def __del__(self):
        self._f.close()
        os.remove(self.path)
