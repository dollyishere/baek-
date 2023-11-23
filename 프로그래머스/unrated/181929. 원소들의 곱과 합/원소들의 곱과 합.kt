class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 1
        val numSum: Int = num_list.sum()
        for (i in 0 until num_list.size) {
            answer *= num_list[i]
        }
        
        if (answer >= (numSum * numSum)) {
            answer = 0
        } else {
            answer = 1
        }
        return answer
    }
}