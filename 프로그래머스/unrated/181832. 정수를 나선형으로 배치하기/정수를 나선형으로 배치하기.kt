class Solution {
    fun solution(n: Int): Array<IntArray> {
        var answer: Array<IntArray> = arrayOf<IntArray>()
        var delta: Array<IntArray> = arrayOf(
    intArrayOf(0, 1),
    intArrayOf(1, 0),
    intArrayOf(0, -1),
    intArrayOf(-1, 0)
)
        var cnt = 1
        var dir = 0
        var i = 0
        var j = 0
        
        repeat(n) { answer += IntArray(n) }
        answer[0][0] = cnt
        while (cnt != n*n) {
            cnt ++
            var flag = true
            while (true) {
                dir = when {
                    i + delta[dir][0] < 0 -> 0
                    j + delta[dir][1] == n -> 1
                    i + delta[dir][0] == n -> 2
                    j + delta[dir][1] < 0 -> 3
                    else -> dir
                }
                var di = i + delta[dir][0]
                var dj = j + delta[dir][1]
                if (answer[di][dj] == 0) {
                    i = di
                    j = dj
                    break
                } else {
                    dir ++
                    if (dir == 4) {
                        dir = 0
                    }
                }
            }
            
            answer[i][j] = cnt
        }
        return answer
    }
}