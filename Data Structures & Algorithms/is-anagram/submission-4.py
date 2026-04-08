class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        print(f's is {s} and t is {t} ')

        if s == t:
            return True
        else:
            return False
        