
class Solution:
    def dfs(self, graph, colors, curr_color, curr_node):
        colors[curr_node] = curr_color
        for adjNode in graph[curr_node]:
            if colors[adjNode] != -1:
                if colors[adjNode] == curr_color:
                    return False
            else:
                ans = self.dfs(graph, colors, 1- curr_color, adjNode)
                if ans == False:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        for i in range(n):
            if colors[i] == -1:
                ans = self.dfs(graph, colors, 0, i)
                if ans == False:
                    return False
        return True