import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int N = friends.length;
        HashMap<String, Integer> idxMap = new HashMap<>();
        for (int i=0;i<N;i++) {
            idxMap.put(friends[i], i);
        }
        
        int[][] record = new int[N][N];
        int[] score = new int[N];
        for (String gift: gifts) {
            String[] temp = gift.split(" ");
            int give = idxMap.get(temp[0]);
            int take = idxMap.get(temp[1]);
            record[give][take]++;
            score[give]++;
            score[take]--;
        }
        
        int answer = 0;
        for (int i=0;i<N;i++) {
            int count = 0;
            for (int j=0;j<N;j++) {
                if (i == j) continue;
                if (record[i][j] > record[j][i] || (record[i][j] == record[j][i] && score[i] > score[j])) {
                    count++;
                }
            }
            answer = Math.max(answer, count);
            
        }
        
        return answer;
    }
}