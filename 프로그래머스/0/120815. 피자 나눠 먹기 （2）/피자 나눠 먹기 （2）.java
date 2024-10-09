class Solution {
    public int solution(int n) {
        int cnt = 6;
        
        while (true) {
            if (cnt % n == 0) {
                break;
            }
            
            cnt += 6;
        }
        
        return cnt / 6;
    }
}