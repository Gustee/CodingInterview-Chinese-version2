# 最长不含重复字符的子字符串
# 从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度
# 假设字符串中只包含a~z的字符，例如
# 在字符串中'arabcacfr'中，最长的不含重复字符的子字符串是'acfr'长度为4

'''
如果第i个字符之前没有出现过，那么f(i)=f(i-1)+1
如果第i个字符之前出现过，计算该字符和它上次出现在字符串中的位置的距离d
1)若d小于等于f(i-1),此时第i个字符粗线量词所夹的子字符串中再也没有重复的字符，则f(i)=d
2)若d>f(i-1)，此时第i个字符上次出现在f(i-1)对应的最长子字符串之前，因此f(i)=f(i-1)+1
'''

class Solution:
    def LongestSubstringWithoutDuplication(self, s):
        # 创建一个长度为26的数组position用来存储每个字符上次出现在字符串中位置的下标。
        lastLength = 0
        curMaxLength = 0
        # 创建一个长度为26的数组position用来存储每个字符上次出现在字符串中位置的下标。
        # -1表示还没有出现过
        position = [-1 for i in range(27)]

        for i in range(len(s)):
            # 该字符上次出现的位置
            preIndex = position[ord(s[i])-ord('a')]
            # 若该字符没有出现过或者d>f(i-1)则f(i-1)+1
            if preIndex < 0 or lastLength < i - preIndex:
                lastLength += 1
            else:
                curMaxLength = max(curMaxLength, lastLength)
                lastLength = i - preIndex
            # 更新position数组
            position[ord(s[i]) - ord('a')] = i
        curMaxLength = max(curMaxLength, lastLength)
        return curMaxLength


if __name__ == '__main__':
    s = Solution()
    x = 'arabcacfr'
    print(s.LongestSubstringWithoutDuplication(x))
