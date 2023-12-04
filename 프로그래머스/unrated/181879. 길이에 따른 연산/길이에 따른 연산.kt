class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        if (num_list.size < 11) {
            answer = 1
        }
        
        for (i in 0 until num_list.size) {
            if (num_list.size >= 11) {
                answer += num_list[i]
            } else {
                answer *= num_list[i]
            }
        }
        return answer
    }
}