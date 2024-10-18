import java.util.ArrayList;

public class Cycledetectiondirected {

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
        graph[0].add(new Edge(0, 1));
        graph[2].add(new Edge(2, 1));
        graph[2].add(new Edge(2, 3));
        graph[3].add(new Edge(3, 4));
        graph[4].add(new Edge(4, 2));
    }

    public static void findNeighbour(ArrayList<Edge> graph[], int index){
        for (int i = 0; i < graph[index].size(); i++){
            Edge e = graph[index].get(i);
            System.out.println("Neighbour of " + e.src + " is " + e.dest);
        }
    }

    public static boolean isCycleDetected(ArrayList<Edge> graph[],boolean vis[],int curr,boolean rec[]){
        vis[curr] = true; rec[curr] = true;
        for (int i = 0; i < graph[curr].size(); i++) {
            Edge e = graph[curr].get(i);
            if(rec[e.dest]){
                return true;
            }
            else if(!vis[e.dest]){
                if(isCycleDetected(graph, vis, e.dest, rec)){
                    return true;
                }
            }
        }
            
        rec[curr] = false;
        return false;
    }

    public static void main(String[] args) {
        /*
         0 ---> 1 <--- 2 <---
                      /      \
                     -> 3 --> 4

        0       1     2       3       4
        0,1          2,1     3,4      4,2
                     2,3      
         */

        int V = 5;
        ArrayList<Edge> graph [] =  new ArrayList[V];
        createGraph(graph);
        boolean ans = isCycleDetected(graph, new boolean[V], V, new boolean[V]);
        System.out.println(ans);
        System.out.println("done");

        //  for (int j = 0; j < V; j++) {   
        //      findNeighbour(graph, j);
        //  }
    }
}
