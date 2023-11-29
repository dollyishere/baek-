class Solution {
    fun solution(my_string: String, indices: IntArray): String {
        var answer: String = ""
        
        for (i in 0 until my_string.length) {
            if (!(i in indices)) {
                answer += my_string[i]
            }    
        }
        
        return answer
    }
}