import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;
import org.w3c.dom.Node;

public class Main {

    static int N;
    static int M;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = Integer.MAX_VALUE;
        for (int j = 0; j < M; j++) {
            for (int k=0;k<3;k++) {
                answer = Math.min(answer, bfs(0, j, k));
            }
        }

        System.out.println(answer);
    }

    static int[][] d = {{1, -1}, {1, 0}, {1, 1}};
    static int bfs(int x, int y, int k) {
        int answer = Integer.MAX_VALUE;
        ArrayDeque<Node> dq = new ArrayDeque<>();
        dq.add(new Node(x, y, graph[x][y], k));
        while (!dq.isEmpty()) {
            Node node = dq.removeFirst();
            for (int _k = 0; _k < 3; _k++) {
                if (_k == node.k) {
                    continue;
                }
                int _x = node.x + d[_k][0];
                int _y = node.y + d[_k][1];
                if (_y < 0 || _y >= M || _x < 0) {
                    continue;
                }
                if (_x == N) {
                    answer = Math.min(answer, node.value);
                    continue;
                }
                dq.add(new Node(_x, _y, node.value + graph[_x][_y], _k));
            }
        }

        return answer;
    }

    static class Node {

        int x;
        int y;
        int value;
        int k;

        Node(int x, int y, int value, int k) {
            this.x = x;
            this.y = y;
            this.value = value;
            this.k = k;
        }
    }


}
