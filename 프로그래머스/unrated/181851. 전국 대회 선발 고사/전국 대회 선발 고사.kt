class Solution {
    fun solution(rank: IntArray, attendance: BooleanArray): Int {
        var checkRank: IntArray = IntArray(3)
        var a: Int = 999
        var b: Int = 999
        var c: Int = 999
        
        for (i in 0 until rank.size) {
            if (attendance[i]) {
                if (a > rank[i]) {
                    c = minOf(c, b)
                    b = minOf(a, b)
                    a = rank[i]
                    checkRank[2] = checkRank[1]
                    checkRank[1] = checkRank[0]
                    checkRank[0] = i
                } else if (b > rank[i]) {
                    c = minOf(c, b)
                    b = rank[i]
                    checkRank[2] = checkRank[1]
                    checkRank[1] = i
                } else if (c > rank[i]) {
                    c = rank[i]
                    checkRank[2] = i
                }
            }    
        }
        
        return 10000 * checkRank[0] + 100 * checkRank[1] + checkRank[2]
    }
}