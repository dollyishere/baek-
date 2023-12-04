class Solution {
    fun solution(myString: String): String {
        var answer: String = ""
        for (i in 0 until myString.length) {
            if (myString[i].equals('a', true)) {
                answer += "A"
            } else {
                answer += myString[i].toLowerCase()
            }
        }
        return answer
    }
}