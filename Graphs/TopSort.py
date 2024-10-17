import queue

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[2].append(Edge(2, 3))
    graph[3].append(Edge(3, 1))
    graph[4].append(Edge(4, 0))
    graph[4].append(Edge(4, 1))
    graph[5].append(Edge(5, 0))
    graph[5].append(Edge(5, 2))

def print_all_neighbours(graph, index):
    for i in graph[index]:
        print(i.dest)

def TopSortUtil(graph, curr, vis, stack):
    vis[curr] = True
    for i in range(len(graph[curr])):
        e = graph[curr][i] 
        if not vis[e.dest]:
            TopSortUtil(graph, e.dest, vis, stack)
    stack.put(curr)

def TopologicalSort(graph, V):
    vis = [False for _ in range(V)]
    stack = queue.LifoQueue()
    for i in range(V):
        if not vis[i]:
            TopSortUtil(graph, i, vis, stack)
        
    while not stack.empty():
        print(stack.get() , end = " ")


def main():
    V = 6
    graph = [[] for _ in range(V)]
    create_graph(graph)

    TopologicalSort(graph, V)
    """
    for j in range(V):
        print(f"Neighbours of {j} is") 
        print_all_neighbours(graph, j)
        print()
    """

if __name__ == "__main__":
    main()