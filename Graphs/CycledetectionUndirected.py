class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1))
    graph[0].append(Edge(0, 4))
    graph[1].append(Edge(1, 0))
    graph[1].append(Edge(1, 2))
    graph[1].append(Edge(1, 4))
    graph[2].append(Edge(2, 1))
    graph[2].append(Edge(2, 3))
    graph[3].append(Edge(3, 2))
    graph[4].append(Edge(4, 0))
    graph[4].append(Edge(4, 1))
    graph[4].append(Edge(4, 5))
    graph[5].append(Edge(5, 4))

def print_all_neighbours(graph, index):
    for i in graph[index]:
        print(i.dest)

def isCycleUndirected(graph, vis, curr, parent):
    vis[curr] = True
    for i in range(len(graph[curr])):
        e = graph[curr][i] 
        if vis[e.dest] and e.dest != parent:
            return True
        elif not vis[e.dest]:
            if isCycleUndirected(graph, vis, e.dest, curr):
                return True
    return False

def main():

    #    1 --- 2 
    #   / |    | 
    #  0  |    3 
    #   \ |
    #    4 ----5
    #      0       1     2       3        4       5
    #      0,1    1,0   2,1     3,2      4,0     5,4   
    #      0,4    1,2   2,3              4,1   
    #             1,4                    4,5   

    V = 6
    graph = [[] for _ in range(V)]
    create_graph(graph)
    vis = [False for _ in range(V)]
    print(isCycleUndirected(graph, vis, 0, -1))

    """
    for j in range(V):
        print(f"Neighbours of {j} is") 
        print_all_neighbours(graph, j)
        print()

    """

if __name__ == "__main__":
    main()