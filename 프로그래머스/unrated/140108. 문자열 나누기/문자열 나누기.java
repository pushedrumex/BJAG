class Solution {
    public int solution(String s) {
        int answer = 0, same = 0, diff = 0;
        char std = ' ';
        boolean flag = false;
        
        for (char c: s.toCharArray()) {
            if (!flag) {
                answer++;
                std = c;
                same = 1;
                diff = 0;
                flag = true;
            } else {
                if (std == c)
                    same++;
                else
                    diff++;
                if (same == diff)
                    flag = false;
            }
        }        
        return answer;
    }
}