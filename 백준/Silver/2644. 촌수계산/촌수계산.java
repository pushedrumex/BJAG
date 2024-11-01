import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[y].add(x);
            graph[x].add(y);
        }

        int answer = -1;
        ArrayDeque<Node> dq = new ArrayDeque<>();
        boolean[] visited = new boolean[n + 1];
        dq.add(new Node(X, 0));
        visited[X] = true;
        while (!dq.isEmpty()) {
            Node node = dq.removeFirst();
            int num = node.num;
            int relation = node.relation;
            if (num == Y) {
                answer = relation;
                break;
            }

            for (int next : graph[num]) {
                if (visited[next]) continue;
                visited[next] = true;
                dq.add(new Node(next, relation + 1));
            }
        }
        System.out.println(answer);

    }

    static class Node {
        int num;
        int relation;

        Node(int num, int relation) {
            this.num = num;
            this.relation = relation;
        }
    }

}