class Solution {
    fun solution(myString: String, pat: String): String {
        var answer: String = ""
        var temp: String = ""
        var last: Int = myString.length - 1
        for (i in myString.length - 1 downTo 0) {
            temp = myString[i] + temp
            if (temp.length == pat.length) {
                if (temp == pat) {
                    answer = myString.slice(0 .. last)
                    break
                } else {
                    temp = temp.slice(0 until temp.length - 1)
                    last --
                }
            }
        }
        return answer
    }
}