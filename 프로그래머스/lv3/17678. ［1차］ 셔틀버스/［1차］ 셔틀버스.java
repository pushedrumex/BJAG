import java.util.*;

class Solution {
    String timeFormat(int m) {        
        int hour = m / 60;
        int minute = m % 60;
        
        String hToStr = "0"+String.valueOf(hour);
        String mToStr = "0"+String.valueOf(minute);
        
        return (hToStr).substring(hToStr.length()-2)+":"+(mToStr).substring(mToStr.length()-2);
    }
    
    public String solution(int n, int t, int m, String[] timetable) {
        int answer = 0;
        int N = timetable.length;
        int start = 9 * 60;
        Deque<Integer> q = new ArrayDeque<>();
        
        Arrays.sort(timetable);
        for (int i=0;i<N;i++) {
            String[] temp = timetable[i].split(":");
            q.add(Integer.parseInt(temp[0]) * 60 + Integer.parseInt(temp[1]));
        }
        
        int i = 0;
        int crewNum = 0, crewTime = 0;
        while (n > i++ && !q.isEmpty()) {
            crewNum = 0;
            answer = start;
            while (!q.isEmpty() && start >= q.peekFirst() && m > crewNum) {
                crewTime = q.removeFirst();
                crewNum++;
            }
            
            if (crewNum == m) {
                answer = crewTime - 1;
            }
            
            start += t;
        }
        
        return timeFormat(answer);
    }
}