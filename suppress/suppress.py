from contextlib import ContextDecorator

class suppress(ContextDecorator):

    def __init__(self, *errs):
        self.errs = errs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.exception = exc_val
        self.traceback = traceback
        if exc_type is not None:
            for err in self.errs:
                if isinstance(exc_val, err):
                    return True
