class Solution {
    fun solution(my_string: String, m: Int, c: Int): String {
        var answer: String = ""
        
        for (i in 0 until my_string.length) {
            if (i % m == c-1) {
                answer += my_string[i]
            }
        }
        
        return answer
    }
}