class Solution {
    fun solution(my_string: String, n: Int): String {
        var answer: String = ""
        answer = my_string.slice((my_string.length - n) until my_string.length)
        return answer
    }
}