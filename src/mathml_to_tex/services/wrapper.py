class Wrapper:
    def __init__(self, op: str, close: str):
        self._open = op
        self._close = close

    def wrap(self, val: str) -> str:
        return self._open + val + self._close

class ParenthesisWrapper(Wrapper):
    def __init__(self):
        super().__init__('\\left(', '\\right)')

    def wrap(self, val: str) -> str:
        return super().wrap(val)

    def wrap_if_more_than_one_char(self, val: str) -> str:
        if len(val) <= 1:
            return val
        return self.wrap(val)

class BracketWrapper(Wrapper):
    def __init__(self):
        super().__init__('{', '}')

    def wrap(self, val: str) -> str:
        return super().wrap(val)