import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        int[] distance = new int[N+1];
        List<int[]>[] graph = new ArrayList[N+1];
        PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        
        for (int i=0;i < N+1;i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int[] temp: road) {
            graph[temp[0]].add(new int[]{temp[1], temp[2]});
            graph[temp[1]].add(new int[]{temp[0], temp[2]});
        }
        
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[1] = 0;
        
        // {거리, 노드}
        q.add(new int[]{0, 1});
        
        while (!q.isEmpty()) {
            int[] now = q.remove();
            
            if (distance[now[1]] < now[0]) continue;
            if (now[0] <= K) answer++;
                
            for (int[] node: graph[now[1]]) {
                int d = node[1] + now[0];
                if (distance[node[0]] > d) {
                    distance[node[0]] = d;
                    q.add(new int[]{d, node[0]});
                }
            }
        }

        return answer;
    }
}