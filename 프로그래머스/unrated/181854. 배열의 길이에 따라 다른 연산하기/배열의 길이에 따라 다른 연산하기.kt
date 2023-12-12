class Solution {
    fun solution(arr: IntArray, n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        for (a in 0 until arr.size) {
            if (arr.size % 2 == 0) {
                if (a % 2 == 1) {
                    answer += (arr[a] + n)
                } else {
                    answer += arr[a]
                }
            } else {
                if (a % 2 == 1) {
                    answer += arr[a]
                } else {
                    answer += (arr[a] + n)
                }
            }
        }
        return answer
    }
}