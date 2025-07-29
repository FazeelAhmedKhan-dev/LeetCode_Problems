class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_count = 0
        for i in range(len(sentences)):
            words = sentences[i].split(" ")
            word_count = max(word_count, len(words))

        return word_count