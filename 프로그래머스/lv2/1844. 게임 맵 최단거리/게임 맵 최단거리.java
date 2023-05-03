import java.util.*;

class Solution {
    int[][] dxdy = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    public int solution(int[][] maps) {
        int N = maps.length, M = maps[0].length;
        Node node;
        Deque<Node> q = new ArrayDeque<>();
        q.addLast(new Node(0,0));
        
        while (!q.isEmpty()) {
            node = q.removeFirst();
            if (node.x == N-1 && node.y == M-1) return maps[node.x][node.y];
            for (int[] d: dxdy) {
                int x = node.x + d[0], y = node.y + d[1];
                if (!(0 <= x && x < N && 0 <= y && y < M) || maps[x][y] == 0) continue;
                if (maps[x][y] > 1) continue;
                maps[x][y] = maps[node.x][node.y]+1;
                q.addLast(new Node(x,y));
            }
        }
        return -1;
    }
    class Node {
        int x,y;
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}