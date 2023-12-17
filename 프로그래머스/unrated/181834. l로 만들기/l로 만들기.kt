class Solution {
    fun solution(myString: String): String {
        var answer: String = ""
        for (s in myString) {
            val result = s.compareTo('l')
            answer += when (result) {
               -1 -> 'l'
                else -> s
            }  
        }
        return answer
    }
}