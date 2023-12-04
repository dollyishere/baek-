class Solution {
    fun solution(my_string: String, alp: String): String {
        var answer: String = ""
        for (i in 0 until my_string.length) {
            if (my_string[i].toString().equals(alp, true)) {
                answer += my_string[i].toUpperCase()
            } else {
                answer += my_string[i]
            }
        }
        return answer
    }
}