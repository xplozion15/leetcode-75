class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        word1_length = len(word1) 
        word2_length = len(word2) 
        merged_string = ""

        while i < word1_length and j < word2_length:
            merged_string += word1[i] + word2[j]
            i += 1
            j += 1

        if i >= word1_length:
            merged_string += word2[j:]
        elif j >= word2_length:
            merged_string += word1[i:]
        return merged_string