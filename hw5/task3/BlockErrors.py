class BlockErrors:
    def __init__(self, err_types):
        self.err_types = err_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type and any(isinstance(exc_value, err_type) for err_type in self.err_types):
            print("Ignoring exception:", exc_value)
            return True
        else:
            return False
