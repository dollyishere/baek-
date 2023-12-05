class Solution {
    fun solution(strArr: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()

        for (i in 0 until strArr.size) {
            var temp: String = ""
            var myString: String = strArr[i]
            var case: Boolean = true
            
            for (j in 0 until myString.length) {
                temp += myString[j]
                if (temp.length == 2) {
                    if (temp == "ad") {
                        case = false
                        break
                    }
                    temp = temp.slice(1 until temp.length)
                }
            }
            
            if (case) {
                answer += myString
            }
        }
        
        return answer
    }
}