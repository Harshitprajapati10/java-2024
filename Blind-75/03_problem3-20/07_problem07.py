# Course Schedule, 207

class Solution:
    def can_complete_courses(self, no_of_vertices, edge_list):
        graph = {}
        vis = [False for _ in range(no_of_vertices)]
        recStack = [False for _ in range(no_of_vertices)]
        for from_node, to_node in edge_list:
            if from_node not in graph:
                graph[from_node] = []
            graph[from_node].append(to_node)
        # if cycle present -> can't complete courses, if no cycle -> complete courses
        for course in range(no_of_vertices):
            if not vis[course]:
                if self._dfs(graph, course, vis, recStack):
                    return False
        return True
    
    # Function to detect cycle
    def _dfs(self,graph, curr, vis, recStack):
        if curr not in graph: return False
        vis[curr] = True
        recStack[curr] = True
        for nei in graph[curr]:
            if recStack[nei]:
                return True
            if not vis[nei]:
                if self._dfs(graph, nei, vis,recStack):
                    return True
        recStack[curr] = False
        return False
    
obj = Solution()    
print(obj.can_complete_courses(2,[[0,1]]))
print(obj.can_complete_courses(2,[[0,1],[1,0]]))
print(obj.can_complete_courses(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))
print(obj.can_complete_courses(3,[[0,1],[1,2],[2,1]]))
