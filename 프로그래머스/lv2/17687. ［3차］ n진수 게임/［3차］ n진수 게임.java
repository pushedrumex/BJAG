class Solution {
    int n;
    
    String nBase(int num) {
        String result = "";
        String[] base = "ABCDEF".split("");
        int rest;
        
        if (num == 0) {
            return "0";
        }
        
        while (num > 0) {
            rest = num % n;
            if (rest > 9) {
                result = base[rest % 10] + result;
            } else {
                result = String.valueOf(rest) + result;
            }
            num = num / n;
        }
        return result;
    }
    
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        String s = "";
        int num = 0;
        int temp = 0;
        this.n = n;
        
        while (s.length() < t*m) {
            s += nBase(num++);
        }
        
        for (int i=0;i<s.length();i++) {
            if (i % m + 1 == p) {
                temp++;
                answer += s.substring(i,i+1);
            }
            if (temp == t) {
                break;
            }
        }
        
        System.out.println(s);

        return answer;
    }
}