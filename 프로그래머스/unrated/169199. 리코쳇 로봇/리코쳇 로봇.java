import java.util.*;

class Solution {
    public int solution(String[] board) {
        int[][] dxdy = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int X = board.length;
        int Y = board[0].length();
        int x, y, cnt, _x, _y;
        ArrayDeque<int[]> q = new ArrayDeque();
        boolean[][] visited = new boolean[X][Y];

        for (int i = 0; i < X; i++) {
            for (int j = 0; j < Y; j++)
                if ('R' == board[i].charAt(j)) {
                    q.addLast(new int[]{i, j, 0});
                    break;
                }
            if (q.size() > 0)
                break;
        }

        while (q.size() > 0) {
            int[] temp = q.removeFirst();
            x = temp[0];
            y = temp[1];
            cnt = temp[2];
            visited[x][y] = true;

            for (int[] d : dxdy) {
                _x = x;
                _y = y;
                while (0 <= _x + d[0] && _x + d[0] < X && 0 <= _y + d[1] && _y + d[1] < Y && 'D' != board[_x + d[0]].charAt(_y + d[1])) {
                    _x += d[0];
                    _y += d[1];
                }

                if (visited[_x][_y])
                    continue;
                else if ('G' == board[_x].charAt(_y))
                    return cnt + 1;
                else
                    q.addLast(new int[]{_x, _y, cnt + 1});
            }
        }
        return -1;
    }
}