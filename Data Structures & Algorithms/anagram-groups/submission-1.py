import utils.session
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sub = []
            sort_word = "".join(sorted(word))
            if sort_word in anagrams:
                anagrams[sort_word].append(word)
            else:
                anagrams[sort_word] = [word]
        return list(anagrams.values())
                



        