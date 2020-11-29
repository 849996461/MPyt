
'''
给定一个字符串 S，找出 S 中不同的非空回文子序列个数，并返回该数字与 10^9 + 7 的模。
通过从 S 中删除 0 个或多个字符来获得子序列。
如果一个字符序列与它反转后的字符序列一致，那么它是回文字符序列。
如果对于某个  i，A_i != B_i，那么 A_1, A_2, ... 和 B_1, B_2, ... 这两个字符序列是不同的。

备注:未能理解解法;
回文串的特征:任意两个相同的回文串在任意地方重叠都会形成一个新的回文串
'''

class Solusion:
    def countPalindromicSubsequences(self, S: str) -> int:
        N = len(S)
        MOD = 1000000007
        nxt = [0] * N
        use = [0] * N
        ans = 0
        for j in range(N):
            x = 1
            for i in range(j - 1, -1, -1):
                if S[i] == S[j]:
                    now_nxt = nxt[i]
                    now_use = use[i]
                    nxt[i] += x
                    x = now_nxt - now_use + 1
                    use[i] = now_nxt + 1
                else:
                    nxt[i] += x
            ans += x
        return ans % MOD