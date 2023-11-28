class Solution {
    fun solution(my_string: String, is_prefix: String): Int {
        var answer: Int = 0
        
        for (i in 1 until my_string.length) {
            var nowS = my_string.slice(0 until i)
            if (nowS == is_prefix) {
                answer = 1
                break
            }
        }
        
        return answer
    }
}