class Solution {
    fun solution(n: Int): Array<IntArray> {
        var answer: Array<IntArray> = arrayOf<IntArray>()
        
        for (i in 0 until n) {
            var nowA: IntArray = IntArray(n)
            nowA[i] = 1
            answer += nowA
        }
        
        return answer
    }
}