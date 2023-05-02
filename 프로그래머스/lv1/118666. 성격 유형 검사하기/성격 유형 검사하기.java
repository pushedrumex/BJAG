import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        Map<String, Integer> map = new HashMap<>();
        for (int i=0;i<survey.length;i++) {
            String[] temp = survey[i].split("");
            int choice = choices[i];
            
            if (choice > 4) {
                map.put(temp[1], map.getOrDefault(temp[1], 0)+choice-4);
            } else if (choice < 4) {
                map.put(temp[0], map.getOrDefault(temp[0], 0)+4-choice);
            }
        }
        
        String answer = "";
        String[] types = {"RT", "CF", "JM", "AN"};
        
        for (String type: types) {
            String[] temp = type.split("");
            if (map.getOrDefault(temp[0], 0) < map.getOrDefault(temp[1], 0)) {
                answer += temp[1];
            } else{
                answer += temp[0];
            }
        }
        return answer;
    }
}