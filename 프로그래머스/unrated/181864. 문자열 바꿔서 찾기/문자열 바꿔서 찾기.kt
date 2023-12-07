class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        var temp: String = ""
        
        outerloop@ for (s in myString) {
            temp += when(s) {
                'A' -> "B"
                else -> "A"
            }

            
            if (temp.length > pat.length) {
                temp = temp.slice(1 until temp.length)
            }
            
            if (temp == pat) {
                answer ++
                break@outerloop
            }
        }
        return answer
    }
}