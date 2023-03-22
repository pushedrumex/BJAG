import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> list = new ArrayList<>();
        int[] answer;
        String[] temp;
        Map<String, Integer> map = new HashMap<>();
        
        for (String term: terms) {
            temp = term.split(" ");
            map.put(temp[0], Integer.parseInt(temp[1]));
        }
        
        for (int i=0;i < privacies.length;i++) {
            temp = privacies[i].split(" ");
            if (today.compareTo(calculate(temp[0], map.get(temp[1]))) >= 0) {
                list.add(i + 1);
            }
        }
        
        answer = new int[list.size()];
        
        for (int i=0;i < list.size(); i++)
            answer[i] = list.get(i);
        
        return answer;
    }
    
    String calculate(String date, int term) {
        String monthString;
        String[] temp = date.split("[.]");
        int month = Integer.parseInt(temp[1]) + term;
        int year = (Integer.parseInt(temp[0])) + month / 12;
        month %= 12;
        
        if (month == 0) {
            month = 12;
             --year;
        }
        monthString = "0" + String.valueOf(month);
        monthString = monthString.substring(monthString.length() - 2, monthString.length());
        return String.join(".", new String[]{String.valueOf(year), monthString, temp[2]});
    }
    
}