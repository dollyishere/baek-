class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = intArrayOf()
        // 가로 세로 최소값 3
        // 노란색 개수는 (가로-2) * (세로-2)
        // 갈색 개수는 (가로 * 2) + (세로 * 2) - 4
        var maxL = (brown + 4) - 3
        var flag = true
        
        for (i in 3..maxL) {
            if (!flag) {
                break
            }
            
            for (j in 3..maxL) {
                if (((i+j) * 2 - 4) == brown && ((i-2) * (j-2)) == yellow) {
                    if (i > j) {
                        answer = intArrayOf(i, j)
                    } else {
                        answer = intArrayOf(j, i)
                    }
                    flag = false
                    break
                }
            }
        }
        
        return answer
    }
}