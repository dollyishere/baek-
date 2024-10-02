import java.util.*;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int[] sortedSides = sides;
        
        Arrays.sort(sortedSides);
        
        int sum = sortedSides[0] + sortedSides[1];

        for (int i=1;i<sum;i++) {
            if (i<sortedSides[1]) {
                if (sortedSides[0]+i <= sortedSides[1]) {
                    continue;
                }
            } else {
                if (i>=sum) {
                    continue;
                }
            }
            
            answer++;
        }
        
        
        return answer;
    }
}