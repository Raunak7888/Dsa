from collections import defaultdict
from functools import lru_cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Step 1: Build mapping (A, B) -> set of possible tops
        rules = defaultdict(set)
        for a, b, c in allowed:
            rules[(a, b)].add(c)

        # Step 2: DFS with memoization
        @lru_cache(None)
        def can_build(row: str) -> bool:
            # Base case: reached the top
            if len(row) == 1:
                return True

            # Generate all possible next rows
            def backtrack(i: int, next_row: list[str]) -> bool:
                if i == len(row) - 1:
                    return can_build("".join(next_row))

                pair = (row[i], row[i + 1])
                if pair not in rules:
                    return False

                for top in rules[pair]:
                    next_row.append(top)
                    if backtrack(i + 1, next_row):
                        return True
                    next_row.pop()

                return False

            return backtrack(0, [])

        return can_build(bottom)
