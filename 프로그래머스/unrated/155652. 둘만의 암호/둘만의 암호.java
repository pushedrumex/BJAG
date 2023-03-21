class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        String alpha = "abcdefghijklmnopqrstuvwxyz";
        int i, temp;
        
        for (char c: s.toCharArray()) {
            temp = index;
            i = alpha.indexOf(c);
            
            while (temp > 0) {
                if (skip.indexOf(alpha.charAt(++i % alpha.length())) == -1) {
                    temp--;
                }
            }
            answer += alpha.charAt(i % alpha.length());
        }
        return answer;
    }
}