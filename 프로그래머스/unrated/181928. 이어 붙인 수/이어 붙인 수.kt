class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        var evenNum: String = ""
        var oddNum: String = ""
        
        for (i in 0 until num_list.size) {
            if (num_list[i] % 2 == 1) {
                oddNum += num_list[i].toString()
            } else {
                evenNum += num_list[i].toString()
            }
        }
        
        answer = evenNum.toInt() + oddNum.toInt()
        return answer
    }
}