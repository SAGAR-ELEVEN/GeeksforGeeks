class Solution:
    def solve(self, n, s):
        active = set()
        seen = set()
        in_use = 0
        rejected = 0

        for ch in s:
            if ch not in seen:
                seen.add(ch)
                if in_use < n:
                    in_use += 1
                    active.add(ch)
                else:
                    rejected += 1
            else:
                if ch in active:
                    in_use -= 1
                    active.remove(ch)

        return rejected
