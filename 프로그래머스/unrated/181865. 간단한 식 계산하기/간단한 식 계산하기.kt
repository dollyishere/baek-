class Solution {
    fun solution(binomial: String): Int {
        var answer: Int = 0
        val parts: List<String> = binomial.split(" ")
        
        answer = when(parts[1]) {
            "+" -> parts[0].toInt() + parts[2].toInt()
            "-" -> parts[0].toInt() - parts[2].toInt()
            else -> parts[0].toInt() * parts[2].toInt()
        }
        return answer
    }
}