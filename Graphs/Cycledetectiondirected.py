class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1))
    graph[2].append(Edge(2, 1))
    graph[2].append(Edge(2, 3))
    graph[3].append(Edge(3, 4))
    graph[4].append(Edge(4, 2))

def print_all_neighbours(graph, index):
    for i in graph[index]:
        print(i.dest)

def isCycleUtil(graph, curr, vis, stack):
    vis[curr] = True
    stack[curr] = True
    for i in range(len(graph[curr])):
        e = graph[curr][i] 
        if stack[e.dest]:
            return True
        elif not vis[e.dest] and isCycleUtil(graph, e.dest,vis, stack):
                return True
    stack[curr] = False
    return False


def isCyclic(graph):
    vis = [False for _ in range(len(graph))]
    for i in range(len(graph)):
        if not vis[i]:
            cycle = isCycleUtil(graph, i , vis, [False for _ in range(len(vis))])
            if(cycle):
                return True
    return False

def main():

    #   0 ---> 1 <--- 2 <---
    #                 /      \
    #                -> 3 --> 4
    #
    #      0       1     2       3       4
    #      0,1          2,1     3,4      4,2
    #                   2,3  

    V = 5
    graph = [[] for _ in range(V)]
    create_graph(graph)
    print(isCyclic(graph))

    """
    for j in range(V):
        print(f"Neighbours of {j} is") 
        print_all_neighbours(graph, j)
        print()
     """

if __name__ == "__main__":
    main()