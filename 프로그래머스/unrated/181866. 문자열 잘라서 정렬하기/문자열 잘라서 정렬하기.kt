class Solution {
    fun solution(myString: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        var temp: String = ""
        
        for (s in myString) {
            if (s == 'x') {
                if (temp != "") {
                    answer += temp
                    temp = ""
                }
            } else {
                temp += s
            }
        }
        
        if (temp != "") {
            answer += temp
        }
        
        answer.sort()
        return answer
    }
}