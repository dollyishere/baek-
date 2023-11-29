class Solution {
    fun solution(n: Int, k: Int): IntArray {
        var answer: IntArray = intArrayOf()
        // step으로 일정 간격 두고 값 올리기
        for (i in k .. n step k) {
            answer += i
        }
        
        return answer
    }
}