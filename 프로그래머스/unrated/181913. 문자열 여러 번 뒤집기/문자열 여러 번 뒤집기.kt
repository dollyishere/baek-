class Solution {
    fun solution(my_string: String, queries: Array<IntArray>): String {
        var answer: String = my_string
        
        queries.forEach { query : IntArray ->
            var startIndex = query[0]
            var endIndex = query[1]
            answer = answer.substring(0 until startIndex) + answer.substring(startIndex .. endIndex).reversed() +  answer.substring(endIndex+1 until answer.length)
        }
        
        return answer
    }
}