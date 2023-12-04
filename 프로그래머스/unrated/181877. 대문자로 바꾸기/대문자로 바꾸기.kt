class Solution {
    fun solution(myString: String): String {
        var answer: String = ""
        for (i in 0 until myString.length) {
            answer += myString[i].toUpperCase()
        }
        return answer
    }
}