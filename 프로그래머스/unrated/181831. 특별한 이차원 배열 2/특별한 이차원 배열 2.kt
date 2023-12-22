class Solution {
    fun solution(arr: Array<IntArray>): Int {
        var answer: Int = 1
        val n: Int = arr.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (arr[i][j] != arr[j][i]) {
                    answer = 0
                    break
                }
            }
        }
        return answer
    }
}