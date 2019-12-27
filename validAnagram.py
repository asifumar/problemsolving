class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        d = {}
        e = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for j in t:
            if j not in e:
                e[j] = 1
            else:
                e[j] += 1

        for key in d.keys():
            if d[key]!=e[key]:
                return False
        return True

