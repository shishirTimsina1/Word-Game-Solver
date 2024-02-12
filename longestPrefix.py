class Solution:
    def longestCommonPrefix(self, strs) -> str:
        firstWord = strs[-1]
        result = ""
        index = 1
        for word in strs:
            if word.startswith(firstWord[0:index]):
                index += 1
                continue
            else:
              break
        return firstWord[0:index-1]


if __name__ == '__main__':
    VBV = Solution()
    strs = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    print(VBV.longestCommonPrefix(strs2))