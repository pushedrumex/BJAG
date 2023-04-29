import java.util.*;

class Solution {
    int k;
    Integer[] output;
    int answer;
    List<List> candidateKey = new ArrayList<>();
    String[][] relation;
    
    public int solution(String[][] relation) {
        k = relation[0].length;
        this.relation = relation;
        for (int i=1;i<k+1;i++) {
            output = new Integer[i];
            combination(i,0,0);
        }
        return answer;
    }
    
    void combination(int n, int cnt, int start) {
        if (n == cnt) {
            check();
            return;
        }
        for (int i=start;i<k;i++) {
            output[cnt] = i;
            combination(n, cnt+1, i+1);
        }
    }
    boolean isDuplicated() {
        for (List<Integer> key: candidateKey) {
            if (Arrays.asList(output).containsAll(key)) {
                return true;
            }
        }
        return false;
    }
    
    boolean isCandidateKey() {
        List<String> tempList = new ArrayList<>();
        for (String[] r: relation) {
            String temp = "";
            for (int i: output) {
                temp += r[i] + " ";
            }
            if (tempList.contains(temp)) {
                return false;
            }
            tempList.add(temp);
        }
        return true;
    }
    
    void check() {
        if (!isDuplicated() && isCandidateKey()) {
            candidateKey.add(Arrays.asList(output.clone()));
            answer++;
        }
    }
}