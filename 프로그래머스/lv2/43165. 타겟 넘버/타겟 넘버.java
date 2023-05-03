class Solution {
    int answer = 0;
    int[] numbers;
    int target;
    int N;
    public int solution(int[] numbers, int target) {
        N = numbers.length;
        this.numbers = numbers;
        this.target = target;
        dfs(0, 0);
        return answer;
    }
    void dfs(int i, int num) {
        if (i == N) {
            if (num == target) answer++;
            return;
        }
        dfs(i+1, num+numbers[i]);
        dfs(i+1, num-numbers[i]);
    }
}