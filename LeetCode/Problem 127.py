from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord  not in wordSet:
            return 0
        q = deque()
        q.append((beginWord, 1))
        while q:
            curr_word, d = q.popleft()
            if curr_word == endWord:
                return d
            for i in range(len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch== curr_word[i]:
                        continue
                    char_change = curr_word[: i] + ch + curr_word[i+1: ]
                    if char_change in wordSet:
                        q.append((char_change, d+1))
                        wordSet.remove(char_change)

        return 0
        