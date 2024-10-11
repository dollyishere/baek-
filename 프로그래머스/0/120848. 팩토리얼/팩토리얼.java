class Solution {
    public int solution(int n) {
        int answer = 1;
        int cnt = 1;
        int sum = 1;
        
        while (true) {
            sum *= cnt;
            if (sum > n) {
                break;
            }
            answer = cnt;
            cnt++;
        }
        
        return answer;
    }
}