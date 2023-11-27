class Solution {
    fun solution(my_string: String, is_suffix: String): Int {
        var answer: Int = 0
        
        for (i in 0 until my_string.length) {
            var nowS = my_string.slice(i until my_string.length).toString()
            if (nowS == is_suffix) {
                answer = 1
                break
            }
        }
        
        return answer
    }
}