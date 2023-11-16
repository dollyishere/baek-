class Solution {
    fun solution(arr: Array<String>): String {
        var answer: String = ""
        for (num in arr.indices) {
            answer += arr[num]
        }
        return answer
    }
}