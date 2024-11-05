from typing import List

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

class GenericWrapper(Wrapper):
    def __init__(self, op: str, close: str):
        open_cmd = f'\\left{op}'
        close_cmd = f'\\right{close}'
        super().__init__(open_cmd, close_cmd)

    def wrap(self, val: str) -> str:
        return super().wrap(val)

class JoinWithManySeparators:
    def __init__(self, separators: list):
        self._separators = separators

    def join(self, arr: List[str]) -> str:
        acc = ''
        for index, current_str in enumerate(arr):
            separator = '' if index == len(arr) - 1 else self._get(index)
            acc += current_str + separator
        return acc


    def _get(self, index: int) -> str:
        if index < len(self._separators):
            return self._separators[index]

        return self._separators[-1] if len(self._separators) > 0 else ','



