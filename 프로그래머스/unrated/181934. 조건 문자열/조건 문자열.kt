class Solution {
    fun solution(ineq: String, eq: String, n: Int, m: Int): Int {
        var answer: Int = 0
        
        // 조건에 따라 realResult 값 설정(Boolean)
        var realResult = when (ineq + eq) {
            ">=" -> n >= m
            "<=" -> n <= m
            ">!" -> n > m
            "<!" -> n < m
            else -> false
        }
        
        // 맞는지 아닌지에 따라 answer 값 변경
        answer = when (realResult) {
            true -> 1
            else -> 0
        }
        
        return answer
    }
}