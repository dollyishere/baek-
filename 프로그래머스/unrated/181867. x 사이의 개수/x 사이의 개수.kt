class Solution {
    fun solution(myString: String): IntArray {
        var answer: IntArray = intArrayOf()
        var num: Int = 0
        for (i in myString) {
            if (i == 'x') {
                answer += num
                num = 0
            } else {
                num ++
            }
        }
        answer += num
        return answer
    }
}