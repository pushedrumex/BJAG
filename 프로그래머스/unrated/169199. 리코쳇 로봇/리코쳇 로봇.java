import java.util.*;

class Solution {
    public int solution(String[] board) {
        int X = board.length, Y = board[0].length();
        int x, y, cnt, _x, _y;
        int[] temp;
        boolean[][] visited = new boolean[X][Y];
        int[][] dxdy = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        Deque<int[]> q = new ArrayDeque();
        
        for (int i=0; i < X; i++) {
            for (int j=0; j < Y; j++)
                if (board[i].charAt(j) == 'R') {
                    q.addLast(new int[]{i, j, 0});
                    break;
                }
            if (!q.isEmpty())
                break;
        }
        
        while (!q.isEmpty()) {
            temp = q.removeFirst();
            x = temp[0];
            y = temp[1];
            cnt = temp[2];
            
            visited[x][y] = true;
            
            for (int[] d: dxdy) {
                _x = x;
                _y = y;
                
                while (_x + d[0] >= 0 && _x + d[0] < X && _y + d[1] >= 0 && _y + d[1] < Y && board[_x + d[0]].charAt(_y + d[1]) != 'D') {
                    _x += d[0];
                    _y += d[1];
                }
                
                if (visited[_x][_y])
                    continue;
                else if (board[_x].charAt(_y) == 'G')
                    return cnt + 1;
                
                q.addLast(new int[]{_x, _y, cnt + 1});
            } 
        }
        return -1;
    }
}