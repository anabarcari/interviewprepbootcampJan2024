class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        return s_freq == t_freq
    
    s = "anagram"
    t = "naparam"