class Solution {
    fun solution(a: Int, b: Int): Long {
        var answer: Long = 0
        var small : Long = 0
        var big : Long = 0
        
        if (a > b) {
            small = b.toLong()
            big = a.toLong()
        } else if (a == b) {
            return a.toLong()
        } else {
            small = a.toLong()
            big = b.toLong()
        }
        
        for (n in small..big) {
            answer += n
        }
        
        return answer
    }
}