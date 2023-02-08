class Solution:
    def countPalindromes(self, s: str) -> int:
        memo = [defaultdict(int), defaultdict(int), [defaultdict(int) for _ in range(10)], [defaultdict(int) for _ in range(10)]]
        out = 0
        for c in s:
            for k in memo[3][int(c)]:
                out += memo[3][int(c)][k]
            for k in memo[2][int(c)]:
                memo[3][int(k[0])][k] += memo[2][int(c)][k]
            for k in memo[1]:
                memo[2][int(k[1])][k] += memo[1][k]
            for k in memo[0]:
                memo[1][k+c] += memo[0][k]
            memo[0][c] += 1
        return out % (10**9 + 7)
