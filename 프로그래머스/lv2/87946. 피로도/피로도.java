import java.util.*;

class Solution {
    int N;
    int k;
    int answer = 0;
    int[][] dungeons;
    boolean[] visited;
    int[] order;
    
    public int solution(int k, int[][] dungeons) {
        this.k = k;
        this.dungeons = dungeons;
        this.N = dungeons.length;
        this.visited = new boolean[N];
        this.order = new int[N];
        
        permutation(0);
        
        return answer;
    }
    
    void permutation(int cnt) {
        if (cnt == N) {
            answer = Math.max(play(), answer);
            return;
        }

        for (int i=0;i<N;i++) {
            if (!visited[i]) {
                visited[i] = true;
                order[cnt] = i;
                permutation(cnt+1);
                visited[i] = false;
            }
        }
    }
    
    int play() {
        int cnt = 0;
        int _k = k;
        for (int i: order) {
            int a = dungeons[i][0];
            int b = dungeons[i][1];
            if (_k >= a) {
                _k -= b;
                cnt++;
            } else {
                break;
            }
        }
        return cnt;
    }
}