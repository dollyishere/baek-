import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        ArrayList<Integer> answerL = new ArrayList<Integer>();
        
        for (int num:numlist) {
            if (num % n == 0) {
                answerL.add(num);
            }
        }
        
        int[] answer = new int[answerL.size()];
        
        for (int i=0; i<answerL.size(); i++) {
            answer[i] = answerL.get(i);
        }
        return answer;
    }
}