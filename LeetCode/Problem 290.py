class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        arr = s.split(" ")

        if len(pattern) != len(arr):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = arr[i]

            if char in hash_map:
                if hash_map[char] != word:
                    return False
            else:
                if word in hash_map.values():
                    return False
                hash_map[char] = word

        return True
