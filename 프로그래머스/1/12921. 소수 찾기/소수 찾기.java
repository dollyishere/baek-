class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i=2;i<=n;i++) {
            int nowN = i;
            Boolean flag = true;
            for (int j=2;j*j<=i;j++) {
                if (nowN%j==0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                answer++;
            }
        }
        
        return answer;
    }
}