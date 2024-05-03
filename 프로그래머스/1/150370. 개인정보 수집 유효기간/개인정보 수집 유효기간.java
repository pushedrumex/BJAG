import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        HashMap<String, Integer> termMap = new HashMap<>();
        for (String term: terms) {
            String[] parsed = term.split(" ");
            termMap.put(parsed[0], Integer.parseInt(parsed[1]) * 28);
        }
        int dayOfToday = convertToDay(today);
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i=0;i<privacies.length;i++) {
            String[] parsed = privacies[i].split(" ");
            int endDay = convertToDay(parsed[0]) + termMap.get(parsed[1]);
            if (dayOfToday >= endDay) {
                answer.add(i+1);
            }
        }
        Collections.sort(answer);
        return answer.stream().mapToInt(i -> i).toArray();
    }
    
    int convertToDay(String s) {
        String[] parsed = s.split("[.]");
        int year = Integer.parseInt(parsed[0]);
        int month = Integer.parseInt(parsed[1]);
        int day = Integer.parseInt(parsed[2]);
        
        return year * 12 * 28 + month * 28 + day;
    }
}