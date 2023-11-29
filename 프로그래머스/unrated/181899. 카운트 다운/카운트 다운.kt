class Solution {
    fun solution(start: Int, end_num: Int): IntArray {
        var answer: IntArray = intArrayOf()
        
        // downTo로 감소
        for (i in start downTo end_num) {
            answer += i
        }
        
        return answer
    }
}