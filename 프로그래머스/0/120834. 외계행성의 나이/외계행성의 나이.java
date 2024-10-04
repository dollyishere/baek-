import java.util.*;

class Solution {
    public String solution(int age) {
        StringBuilder answer = new StringBuilder();
        String changeNum = Integer.toString(age);
        
        for (int i=0;i<changeNum.length();i++) {
            int nowNum = Character.getNumericValue(changeNum.charAt(i));
            answer.append((char) (nowNum + 'a')); 
        }
        return answer.toString();
    }
}