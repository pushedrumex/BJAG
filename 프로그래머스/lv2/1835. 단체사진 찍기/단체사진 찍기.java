import java.util.*;

class Solution {
    int answer = 0;
    Map<String, Integer> map = new HashMap<>();
    String[] arr = {"A", "C", "F", "J", "M", "N", "R", "T"};
    int N = arr.length;
    int[] order = new int[N];
    boolean[] visited = new boolean[N];
    Condition[] conditions;
    
    public int solution(int n, String[] data) {
        conditions = new Condition[n];
        for (int i=0;i<n;i++) {
            String[] temp = data[i].split("");
            conditions[i] = new Condition(temp[0], temp[2], temp[3], Integer.parseInt(temp[4]));
        }
        permutation(0);
        return answer;
    }
    
    void permutation(int cnt) {
        if (cnt == N) {
            answer += checkOrder();
            return;
        }
        for (int i=0;i<N;i++) {
            if (visited[i]) continue;
            order[cnt] = i;
            visited[i] = true;
            permutation(cnt+1);
            visited[i] = false;
        }
    }
    
    int checkOrder() {
        String[] temp;
        for (int i=0;i<N;i++) {
            map.put(arr[i], order[i]);
        }
        for (Condition condition: conditions) {
            int dist = Math.abs(map.get(condition.p1)-map.get(condition.p2))-1;
            
            switch(condition.sign) {
                case "=":
                    if (dist != condition.dist) {
                        return 0;
                    }
                    break;
                case ">":
                    if (!(dist > condition.dist)) {
                        return 0;
                    }
                    break;
                case "<":
                    if (!(dist < condition.dist)) {
                        return 0;
                    }
                    break;
            }
        }
        return 1;
    }
    
    class Condition {
        String p1;
        String p2;
        String sign;
        int dist;
        
        Condition(String p1, String p2, String sign, int dist) {
            this.p1 = p1;
            this.p2 = p2;
            this.sign = sign;
            this.dist = dist;
        }
    }
}