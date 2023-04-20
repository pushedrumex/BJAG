import java.util.*;

class Solution {
    void fallDown(int m, int n, String[][] board) {
        for (int j = 0; j < n; j++) {
            String col = "";
            
            for (int k = 0; k < m; k++) {
                col += "X";
            }

            
            for (int i = 0; i < m; i++) {
                if (!board[i][j].equals("X")) {
                    col += board[i][j];
                }
            }
            col = col.substring(col.length() - m);
            String[] col_temp = col.split("");
            for (int i = m-1; i >= 0; i--) {
                board[i][j] = col_temp[i];
            }
        }
    }

    // 지워진 블록은 X
    int removeBlock(int m, int n, String[][] board) {
        boolean[][] visited = new boolean[m][n];
        int result = 0;
        int[][] dxdy = new int[][]{{0, 0}, {0, 1}, {1, 1}, {1, 0}};

        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                String shape = board[i][j];

                if (shape.equals("X")) {
                    continue;
                }

                boolean flag = true;
                for (int[] d : dxdy) {
                    if (!board[i + d[0]][j + d[1]].equals(shape)) {
                        flag = false;
                        break;
                    }
                }
                // 4개 블록 동일
                if (flag) {
                    for (int[] d : dxdy) {
                        if (!visited[i + d[0]][j + d[1]]) {
                            visited[i + d[0]][j + d[1]] = true;
                            result++;
                        }
                    }
                }
            }
        }

        // 방문한 블록들 'X'처리
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) {
                    board[i][j] = "X";
                }
            }
        }

        return result;
    }

    public int solution(int m, int n, String[] board) {
        int answer = 0;
        int temp = 0;
        String[][] _board = new String[m][];

        for (int i = 0; i < m; i++) {
            _board[i] = board[i].split("");
        }

        while (true) {
            temp = removeBlock(m, n, _board);
            if (temp == 0) {
                break;
            }
            fallDown(m, n, _board);
            answer += temp;
        }

        return answer;
    }
}