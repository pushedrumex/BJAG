class Solution {
    int answer, same, diff;
    char c;
    boolean flag;
    
    public int solution(String s) {
        for (int i=0;i < s.length();i++) {
            if (!flag) {
                c = s.charAt(i);
                same = 1;
                diff = 0;
                flag = true;
            } else {
                if (c == s.charAt(i))
                    same++;
                else
                    diff++;
                
                if (same == diff) {
                    answer++;
                    flag = false;
                }
            }
        }
        if (same != diff)
            answer++;
        
        return answer;
    }
}