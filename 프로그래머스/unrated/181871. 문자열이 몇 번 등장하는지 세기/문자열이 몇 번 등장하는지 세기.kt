class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        var temp: String = ""
        
        for (i in 0 until myString.length) {
            temp += myString[i]
            if (temp.length == pat.length) {
                if (temp == pat) {
                    answer ++
                }
                temp = temp.slice(1 until temp.length)
            }
        }
        
        return answer
    }
}