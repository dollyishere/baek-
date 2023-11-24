class Solution {
    fun solution(n: Int, control: String): Int {
        var answer: Int = n
        
        for (i in 0 until control.length) {
            if (control[i].toString() == "w") {
                answer ++
            }
            if (control[i].toString() == "s") {
                answer --
            }
            if (control[i].toString() == "d") {
                answer += 10
            }
            if (control[i].toString() == "a") {
                answer -= 10
            }
        }
        
        return answer
    }
}