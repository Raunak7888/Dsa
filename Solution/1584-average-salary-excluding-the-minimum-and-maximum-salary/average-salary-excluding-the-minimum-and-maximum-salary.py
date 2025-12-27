class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = min(salary)
        max_sal = max(salary)
        salary_sum = sum(salary) - min_sal - max_sal
        return salary_sum / (len(salary)-2)

        