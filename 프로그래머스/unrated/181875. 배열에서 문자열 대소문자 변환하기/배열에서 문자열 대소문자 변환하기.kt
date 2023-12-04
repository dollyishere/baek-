class Solution {
    fun solution(strArr: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (i in 0 until strArr.size) {
            if (i % 2 == 0) {
                answer += strArr[i].toLowerCase()
            } else {
                answer += strArr[i].toUpperCase()
            }
        }
        return answer
    }
}