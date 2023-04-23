import java.util.*;

class Solution {
    int[][] picture;
    int m, n;
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int temp = 0;
        int[] answer = new int[2];
        
        this.picture = new int[m][n];
        for (int i=0;i<m;i++)
            for (int j=0;j<n;j++)
                this.picture[i][j] = picture[i][j];

        this.m = m;
        this.n = n;
        
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if (this.picture[i][j] > 0) {
                    numberOfArea++;
                    temp = bfs(i, j);
                    if (maxSizeOfOneArea < temp) {
                        maxSizeOfOneArea = temp;
                    }
                }
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
    
    int bfs(int i, int j) {
        int[][] dxdy = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        int _i, _j;
        int cnt = 1;
        int color = picture[i][j];
        
        picture[i][j] = 0;
        Node node;
        Deque<Node> q = new ArrayDeque<>();
        q.addLast(new Node(i, j));
        
        while (!q.isEmpty()) {
            node = q.removeFirst();
            for (int[] d: dxdy) {
                _i = node.i + d[0];
                _j = node.j + d[1];

                if (!(0 <= _i && _i < m && 0 <= _j && _j < n) || picture[_i][_j] == 0) continue;

                if (color == picture[_i][_j]) {
                    cnt++;
                    picture[_i][_j] = 0;
                    q.addLast(new Node(_i, _j));
                }
            }
        }
        return cnt;
    }
    
    class Node {
        int i, j;
        
        Node(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}