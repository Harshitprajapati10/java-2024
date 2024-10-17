import java.util.ArrayList;
import java.util.Stack;

public class TopSort{ // for DAGs

    static class Edge {
        int src;
        int dest;

        public Edge(int s, int d) {
            this.src = s;
            this.dest = d;
        }
    }

    static void createGraph(ArrayList<Edge> graph[]){
        for (int i = 0; i < graph.length; i++) {
            graph[i] = new ArrayList<Edge>();
        }
        graph[2].add(new Edge(2, 3));
        graph[3].add(new Edge(3, 1));
        graph[4].add(new Edge(4, 0));
        graph[4].add(new Edge(4, 1));
        graph[5].add(new Edge(5, 0));
        graph[5].add(new Edge(5, 2));
    }

    public static void findNeighbour(ArrayList<Edge> graph[], int index){
        for (int i = 0; i < graph[index].size(); i++){
            Edge e = graph[index].get(i);
            System.out.println("Neighbour of " + e.src + " is " + e.dest);
        }
    }

    public static void TopSortUtil(ArrayList<Edge> graph[], int curr, boolean vis[], Stack<Integer> stack){
        vis[curr] = true;
        for (int i = 0; i < graph[curr].size(); i++){
            Edge e = graph[curr].get(i);
            if(!vis[e.dest]){
                TopSortUtil(graph, e.dest, vis, stack);
            }
        }
        stack.push(curr); // 0 1 3 2 4 5
    }

    public static void TopologicalSort(ArrayList<Edge> graph[], int V){
        boolean vis[] = new boolean[V];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < V; i++) {
            if(!vis[i]){
                TopSortUtil(graph, i, vis, stack);
            }
        }
        while(!stack.isEmpty()){
            System.out.print(stack.pop() + " ");
        }
    }
    public static void main(String[] args) {

        /*
         5 -----> 0 <---- 4
         |                |
         |                | 
         -> 2 --> 3 --> 1<-

          5  4  2  3  1  0

          graph = 0   1    2     3    4     5
                           2,3  3,1   4,0  5,0  
                                      4,1  5,2
         */

        int V = 6;
        ArrayList<Edge> graph [] =  new ArrayList[V];
        createGraph(graph);

        TopologicalSort(graph, V);

        //  for (int j = 0; j < V; j++) {   
        //      findNeighbour(graph, j);
        //  } 
    }
}