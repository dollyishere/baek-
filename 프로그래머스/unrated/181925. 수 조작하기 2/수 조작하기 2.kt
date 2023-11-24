class Solution {
    fun solution(numLog: IntArray): String {
        var answer: String = ""
        var firstNum: Int = numLog[0]
        
        for (i in 1 until numLog.size) {
            if (firstNum + 1 == numLog[i]) {
                answer += "w"
            }    
            if (firstNum - 1 == numLog[i]) {
                answer += "s"
            }   
            if (firstNum + 10 == numLog[i]) {
                answer += "d"
            }   
            if (firstNum - 10 == numLog[i]) {
                answer += "a"
            }  
            firstNum = numLog[i]
        }
        
        return answer
    }
}