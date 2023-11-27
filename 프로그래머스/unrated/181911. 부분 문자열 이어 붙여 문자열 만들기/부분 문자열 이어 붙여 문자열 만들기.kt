class Solution {
    fun solution(my_strings: Array<String>, parts: Array<IntArray>): String {
        var answer: String = ""
        
        for (i in 0 until my_strings.size) {
            var nowS = my_strings[i]
            var nowP = parts[i]
            
            answer += nowS.slice(nowP[0] .. nowP[1])
        }
        
        return answer
    }
}