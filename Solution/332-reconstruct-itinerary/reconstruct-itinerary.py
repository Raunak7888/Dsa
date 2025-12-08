class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        

        for src in graph: 
            graph[src].sort(reverse=True)

        route = []

        def dfs(airport):
            dest = graph[airport]

            while dest:
                curr = dest.pop()
                dfs(curr)
            route.append(airport)

        dfs("JFK")

        route.reverse()
        return route



        return route