// 나가는 것만 있고, 나가는 것의 개수가 가장 많은 것이 생성한 정점
// 도넛: 노드 개수 == 전선 개수
// 막대: 노드 개수 - 1  == 전선 개수
// 팔자: 노드 개수 + 1 == 전선개수

import java.util.*;

class Solution {
    int newNode = 0;
    int donut = 0;
    int rod = 0;
    int eight = 0;
    HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
    
    public int[] solution(int[][] edges) {
        HashMap<Integer, Boolean> inMap = new HashMap<>();
        
        for (int[] edge: edges) {
            int start = edge[0];
            int end = edge[1];
            ArrayList<Integer> temp = graph.getOrDefault(start, new ArrayList<>());
            temp.add(end);
            graph.put(start, temp);
            inMap.put(end, true);
        }
        
        int inMaxCount = 0;
        for (int i: graph.keySet()) {
            if (inMap.containsKey(i)) continue;
            if (graph.get(i).size() > inMaxCount) {
                inMaxCount = graph.get(i).size();
                newNode = i;
            }   
        }
        for (int i: graph.get(newNode)) {
            Count count = getCount(i);
            if (count.edge == count.node) {
                donut++;
            } else if (count.edge == count.node - 1) {
                rod++;
            } else if (count.edge == count.node + 1) {
                eight++;
            }
        }
        
        int[] answer = {newNode, donut, rod, eight};
        return answer;
    }
    
    Count getCount(int start) {
        int node = 1;
        int edge = 0;
        
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        HashMap<Integer, Boolean> visited = new HashMap<>();
        dq.add(start);
        visited.put(start, true);
        while (!dq.isEmpty()) {
            int now = dq.removeFirst();
            for (int next: graph.getOrDefault(now, new ArrayList<Integer>())) {
                edge++;
                if (!visited.containsKey(next)) {
                    visited.put(next, true);
                    node++;
                    dq.addLast(next);
                }
            }
        }
        return new Count(node, edge);
    }
    
    class Count {
        int node;
        int edge;
        
        Count(int node, int edge) {
            this.node = node;
            this.edge = edge;
        }
    }
}