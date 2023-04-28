import java.util.*;

class Solution {
    int n, m, r, c;
    int _x,_y;
    int[][] dxdy = {{1,0},{0,-1},{0,1},{-1,0}};
    String[] direction = "dlru".split("");
    String pathTemp;

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        this.n = n;
        this.m = m;
        this.r = r;
        this.c = c;

        String answer = dfs(x, y, k, "");
        if (answer == null) {
            return "impossible";
        }
        return answer;
    }

    String dfs(int x, int y, int k, String path) {
        int diff = Math.abs(x-r)+Math.abs(y-c);
        if (diff > k) return null;
        if ((k - diff)%2 != 0) return null;
        if (k == 0) return path;
        
        for (int i=0;i<4;i++) {
            int[] d = dxdy[i];
            _x = x + d[0];
            _y = y + d[1];
            if (!(0 < _x && _x <= n && 0 < _y && _y <= m)) continue;
            pathTemp = dfs(_x, _y, k-1, path+direction[i]);
            if (pathTemp != null) return pathTemp;
        }
        return null;
    }
}