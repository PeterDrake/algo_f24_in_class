class BruteForceSearch():
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        for i in range(len(text) - len(self.pattern) + 1):
            for j in range(len(self.pattern)):
                if text[i + j] == self.pattern[j] and j == len(self.pattern)-1:
                    return i
                if text[i + j] != self.pattern[j]:
                    break
        return -1