class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)

        hash_map = {}
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1

        result = []

        for offset in range(word_len):
            i = offset
            while i + total_len <= s_len:
                sub_str = s[i: i + total_len]
                
                chunks = [sub_str[j:j+word_len] for j in range(0, total_len, word_len)]

                seen = {}
                valid = True

                for word in chunks:
                    if word in hash_map:
                        seen[word] = seen.get(word, 0) + 1
                        if seen[word] > hash_map[word]:
                            valid = False
                            break
                    else:
                        valid = False
                        break

                if valid:
                    result.append(i)

                i += word_len 

        return result
