class Solution {
    fun solution(arr: IntArray, flag: BooleanArray): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in 0 until arr.size) {
            if (flag[i]) {
                for (a in 0 until (arr[i] * 2)) {
                    answer += arr[i]
                }
            } else {
                answer = answer.toList().slice(0 until (answer.size - arr[i])).toIntArray()
            }
        }
        return answer
    }
}