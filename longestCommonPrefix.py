from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min([len(i) for i in strs])

        for i in range(0,mini):
            temp = strs[0][i]

            for j in range(1, len(strs)):
                if temp!= strs[j][i]:
                    return strs[0][:i]
        return strs[0]

test = Solution()
s = ["flower","flow","flight"]
print(test.longestCommonPrefix(s))
