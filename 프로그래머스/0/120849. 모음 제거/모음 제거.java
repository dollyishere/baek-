import java.util.*;

class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        for (int i=0;i<my_string.length();i++) {
            char s = my_string.charAt(i);
            if (s == 'o' || s == 'u' || s == 'i' || s == 'e' || s == 'a') {
                continue;
            }
            answer.append(s);
        }
        return answer.toString();
    }
}