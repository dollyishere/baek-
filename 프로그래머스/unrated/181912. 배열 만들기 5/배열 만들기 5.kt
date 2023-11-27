class Solution {
    fun solution(intStrs: Array<String>, k: Int, s: Int, l: Int): IntArray {
        var answer: IntArray = intArrayOf()
        
        for (i in 0 until intStrs.size) {
            var nowStr = intStrs[i].slice(s..s+l-1).toInt()
            if (nowStr > k) {
                answer += nowStr
            }
        }
        return answer
    }
}