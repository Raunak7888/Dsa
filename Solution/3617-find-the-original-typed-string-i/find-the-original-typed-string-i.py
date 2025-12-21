class Solution:
    def possibleStringCount(self, word: str) -> int:
        a = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                a+=1
        return a