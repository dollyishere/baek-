class Solution {
    public String solution(String s, int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        for (int i=0;i<s.length();i++) {
            char nowS = s.charAt(i);
            
            if (nowS == ' ') {
                sb.append(' ');
                continue;
            }
            
            int over = 65;
            if (nowS >= 97) {
                over = 97;
            }
            if (nowS >= 'A' && nowS <= 'Z') {
                sb.append((char) ((nowS - 'A' + n) % 26 + 'A'));
            }
            else if (nowS >= 'a' && nowS <= 'z') {
                sb.append((char) ((nowS - 'a' + n) % 26 + 'a'));
            }
        }
        
        return sb.toString();
    }
}