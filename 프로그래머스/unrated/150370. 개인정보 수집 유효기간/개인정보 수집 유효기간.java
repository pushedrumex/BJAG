import java.util.*;

class Solution {
    int convert(String date) {
        String[] temp = date.split("[.]");
        int year = Integer.parseInt(temp[0].substring(2, 4));
        int month = Integer.parseInt(temp[1]);
        int day = Integer.parseInt(temp[2]);
        
        return year*12*30+month*30+day;
    }
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        
        for (String term: terms) {
            String[] temp = term.split(" ");
            map.put(temp[0], Integer.parseInt(temp[1])*30);
        }
        
        int todayConverted = convert(today);
        for (int i=0;i<privacies.length;i++) {
            String[] temp = privacies[i].split(" ");
            int destroy = convert(temp[0]) + map.get(temp[1]);
            if (todayConverted >= destroy) answer.add(i+1);
        }
        
        return answer.stream().mapToInt(integer -> integer).toArray();
    }
}