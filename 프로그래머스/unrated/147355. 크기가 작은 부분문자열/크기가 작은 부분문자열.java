class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int pl = p.length(), tl = t.length();
        
        for (int i=0;i<=tl-pl;i++) {
            if (t.substring(i, i+pl).compareTo(p) <= 0)
                answer++;
        }
        return answer;
    }
}