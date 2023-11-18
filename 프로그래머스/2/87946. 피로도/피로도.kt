class Solution {
    private var answer: Int = -1
    private var visitedCnt : Int = 0
    private var goDungeons = BooleanArray(8)
    
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        for (i in dungeons.indices) {
            dfs(k, i, dungeons)
        }
        return answer
    }
    
    fun dfs(can_use : Int, now : Int, dungeons: Array<IntArray>) {
        goDungeons[now] = true
        visitedCnt ++
        
        if (visitedCnt > answer) {
            answer = visitedCnt
        }
        
        for (i in dungeons.indices) {
            if (!goDungeons[i] && ((can_use-dungeons[now][1]) >= dungeons[i][0])) {
                dfs(can_use-dungeons[now][1], i, dungeons)
            }
        }
        
        goDungeons[now] = false
        visitedCnt --
    }
}