class Solution {
    fun solution(rny_string: String): String {
        var answer: String = ""
        for (s in rny_string) {
            if (s == 'm') {
                answer += "rn"
            } else {
                answer += s
            }
        }
        return answer
    }
}