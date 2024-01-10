class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        var num = n.toString()

        for (i in 0 until num.length) {
            answer += num[i].toString().toInt()
        }
        return answer
    }
}