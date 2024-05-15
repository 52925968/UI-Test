class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        next1 = [0] * (len(needle) + 1)
        next1[0] = -1
        k = -1
        j = 0
        while(j < len(needle)):
            if (k == -1 or needle[j] == needle[k]):
                j += 1
                k += 1
                next1[j] = k
            else:
                k = next1[k]

        n = 0
        jj = 0
        while n < len(needle) and jj < len(haystack):
            if (n < 0 or haystack[jj] == needle[n]):
                n += 1
                jj += 1
            else:
                n = next1[n]

        if (n == len(needle)):
            return (jj - n)
        else:
            return -1

if __name__=="__main__":
    print(Solution().strStr("aabaaabaaac", "aabaaac"))