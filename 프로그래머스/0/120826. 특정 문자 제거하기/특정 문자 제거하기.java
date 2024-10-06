import java.util.*;

class Solution {
    public String solution(String my_string, String letter) {
        StringBuilder answer = new StringBuilder();
        
        for (int i=0;i<my_string.length();i++) {
            String nowS = my_string.substring(i, i+1);
            
            if (!nowS.equals(letter)) {
                answer.append(nowS);
            }
        }
        
        return answer.toString();
    }
}