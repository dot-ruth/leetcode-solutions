class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}
        for word in strs:
            word_key = ''.join(sorted(word))
            if word_key in anagram:
                anagram[word_key].append(word)
            else: 
                anagram[word_key] = [word]
        return list(anagram.values())
        