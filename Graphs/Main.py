import queue

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    for i in range(len(graph)):
        graph[i] = []
    
    graph[0].append(Edge(0, 1))
    graph[0].append(Edge(0, 2))
    graph[1].append(Edge(1, 3))
    graph[1].append(Edge(1, 0))
    graph[2].append(Edge(2, 0))
    graph[2].append(Edge(2, 4))
    graph[3].append(Edge(3, 1))
    graph[3].append(Edge(3, 4))
    graph[3].append(Edge(3, 5))
    graph[4].append(Edge(4, 2))
    graph[4].append(Edge(4, 3))
    graph[4].append(Edge(4, 5))
    graph[5].append(Edge(5, 4))
    graph[5].append(Edge(5, 3))
    graph[5].append(Edge(5, 6))
    graph[6].append(Edge(6, 5))


def print_all_neighbours(graph, index):
    for i in graph[index]:
        print(i.dest)


def bfs(graph, V):
    q = queue.Queue()
    vis = [False for _ in range(V)]
    q.put(0)
    while not q.empty():
        curr = q.get()
        if vis[curr] == False:
            print(f"{curr}" , end=" ")
            vis[curr] = True
            for i in range(len(graph[curr])):
                e = graph[curr][i]       
                q.put(e.dest)  


def dfs(graph, curr , vis):
    print(curr, end = " ")
    vis[curr] = True
    for i in range(len(graph[curr])):
        e = graph[curr][i]       
        if not vis[e.dest]:
            dfs(graph, e.dest, vis)

def find_all_paths(graph, vis, curr, path, tar):
    if curr == tar:
        print(path)
        return
    for i in range(len(graph[curr])):
        e = graph[curr][i]       
        if not vis[e.dest]:
            vis[curr] = True
            find_all_paths(graph, vis, e.dest, path+f"{e.dest}" , tar)
            vis[curr] = False


def main():

    #   1 --- 3
    #  /     | \
    # 0      |  5
    # \      | / \
    #  2 --- 4    6

    # Graph is in this form of adjacency list
    #  0    1   2    3    4    5    6
    # 0,1  1,3 2,0  3,1  4,2  5,3  6,5
    # 0,2  1,0 2,4  3,4  4,3  5,4
    #               3,5  4,5  5,6

    V = 7
    graph = [[] for _ in range(V)]
    create_graph(graph)

    # bfs(graph, V)

    # vis = [False for _ in range(V)]
    # dfs(graph, 0, vis)

    #Find all paths between given source and target
    src = 0
    tar = 5
    vis = [False for _ in range(V)]
    find_all_paths(graph, vis, src , "0", tar)

    #Finding all neighbours
    """
    for j in range(V):
        print(f"Neighbours of {j} is") 
        print_all_neighbours(graph, j)
        print()
    """


if __name__ == "__main__":
    main()