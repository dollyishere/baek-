import java.util.*;

public class Solution {
    public static int solution(int[] array) {
        HashMap<Integer, Integer> cntMap = new HashMap<>();
        int maxCnt = 0;
        int mode = -1;
        int modeCnt = 0;
        
        for (int num: array) {
            cntMap.put(num, cntMap.getOrDefault(num, 0) + 1);
            int crrCnt = cntMap.get(num);
            
            if (crrCnt > maxCnt) {
                maxCnt = crrCnt;
                mode = num;
                modeCnt = 1;
            } else if (crrCnt == maxCnt) {
                modeCnt++;
            }
        }
        
        return modeCnt == 1 ? mode : -1;
    }
}