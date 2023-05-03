class Solution {
    boolean[] visited;
    int N, M;
    int[][] computers;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        this.computers = computers;
        N = computers.length;
        visited = new boolean[N];

        for (int i=0;i<N;i++) {
            if (!visited[i]) {
                visited[i] = true;
                answer++;
                dfs(i);
            }
        }
        return answer;
    }
    
    void dfs(int i) {
        for (int j=0;j<N;j++) {
            if (computers[i][j] == 1 && !visited[j]) {
                visited[j] = true;
                dfs(j);
            }
        }
    }
}