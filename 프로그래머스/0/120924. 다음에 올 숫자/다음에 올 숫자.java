class Solution {
    public int solution(int[] common) {
        int answer = 0;
        
        int plusV = common[1] - common[0];
        int multiV = 0;
        boolean flag = true;
        
        for (int i=1;i<common.length;i++) {
            
            if (common[i-1] == 0) {
                if (common[i] == 0) {
                    break;
                }
                flag = false;
                break;
            }
            
            if (common[i] % common[i-1] == 0) {
                multiV = common[i] / common[i-1];
            } else {
                flag = false;
                break;
            }
        }
        
        if (flag) {
            answer = common[common.length-1] * multiV;
        } else {
            answer = common[common.length-1] + plusV;
        }
        
        return answer;
    }
}