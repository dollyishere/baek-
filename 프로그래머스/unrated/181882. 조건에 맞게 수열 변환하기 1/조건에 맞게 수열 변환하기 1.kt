class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = arr
        for (i in 0 until arr.size) {
            if (arr[i] >= 50 && arr[i] % 2 == 0) {
                answer[i] /= 2
            } else if (arr[i] < 50 && arr[i] % 2 == 1) {
                answer[i] *= 2
            }
        }
        return answer
    }
}