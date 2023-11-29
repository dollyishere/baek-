class Solution {
    fun solution(arr: IntArray, idx: Int): Int {
        var answer: Int = -1
        for (i in 0 until arr.size) {
            if (i >= idx && arr[i] == 1) {
                answer = i
                break
            }
        }
        return answer
    }
}