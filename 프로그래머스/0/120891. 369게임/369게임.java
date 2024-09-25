import java.util.*;

class Solution {
    public int solution(int order) {
        int answer = 0;
        int copyOrder = order;
        int cnt = (int) Math.pow(10, String.valueOf(order).length()-1);

        while (cnt > 0) {
            int nowN = copyOrder / cnt;
            
            if (nowN % 3 == 0 && nowN != 0) {
                answer++;
            }
            copyOrder -= (nowN * cnt);
            cnt /= 10;
        }
        
        
        return answer;
    }
}