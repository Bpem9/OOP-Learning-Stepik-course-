class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = s
        self.romdict = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        self.res = self.romdict[self.s[-1]]
        for i in range(len(self.s)-1):
            if self.romdict[self.s[i]] < self.romdict[self.s[i+1]]:
                self.res -= self.romdict[self.s[i]]
            else:
                self.res += self.romdict[self.s[i]]
        return self.res
s = Solution().romanToInt('MCMXCIV')
print(s)
