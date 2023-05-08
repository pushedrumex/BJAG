// 왼쪽에서 접근 or 위쪽에서 접근
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int MOD = 1000000007;
        long[][] dp = new long[n][m];
        boolean[][] graph = new boolean[n][m];
        
        for (int[] puddle: puddles) {
            graph[puddle[1]-1][puddle[0]-1] = true;
        }
        
        for (int i=0;i<m;i++) {
            if (graph[0][i]) break;
            dp[0][i] = 1;
        }
        
        for (int i=0;i<n;i++) {
            if (graph[i][0]) break;
            dp[i][0] = 1;
        }
        
        for (int i=1;i<n;i++) {
            for (int j=1;j<m;j++) {
                if (graph[i][j]) continue;
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
            }
        }
        
        return (int)dp[n-1][m-1];
    }
}