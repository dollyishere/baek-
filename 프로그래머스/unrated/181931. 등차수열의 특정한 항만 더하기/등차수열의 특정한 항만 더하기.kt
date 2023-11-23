class Solution {
    fun solution(a: Int, d: Int, included: BooleanArray): Int {
        var answer: Int = 0
        var nowNum : Int = a
        
        for (i in 0 until included.size) {
            if (included[i]) {
                answer += nowNum
            }
            nowNum += d
        }
        
        return answer
    }
}