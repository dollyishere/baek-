import java.util.*;

class Solution {
    private char makeWin(char nowA) {
        char returnV = '0';
        
        switch (nowA) {
            case '0':
                returnV = '5';
                break;
            case '2':
                returnV = '0';
                break;
            case '5':
                returnV = '2';
                break;
            default:
                break;
        }
        
        return returnV;
    }

    
    public String solution(String rsp) {
        StringBuilder answer = new StringBuilder();
        
        for (int i=0;i<rsp.length();i++) {
            answer.append(makeWin(rsp.charAt(i)));
        }
        
        return answer.toString();
    }
}