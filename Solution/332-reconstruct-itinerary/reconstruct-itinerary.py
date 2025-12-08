class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        loc = defaultdict(list)
        for arv, des in sorted(tickets, reverse=True):
            loc[arv].append(des)
        for src in loc:
            loc[src].sort(reverse=True)
        res = []
        def dfs(node):
            dest = loc[node]
            while dest:
                cur = dest.pop()
                dfs(cur)
            res.append(node)
        dfs("JFK")

        return res[::-1]
