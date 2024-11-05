class WhiteSpaceNormalizer:
    def normalize(self, string: str) -> str:
        return ' '.join(string.split())