class Solution {
    fun solution(my_string: String, k: Int): String {
        var answer: String = ""
        
        for (x in 1..k) {
            answer += my_string
        }
        
        return answer
    }
}