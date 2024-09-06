class Solution {
    fun solution(id_pw: Array<String>, db: Array<Array<String>>): String {
        var answer: String = "fail"
        var flag: Boolean = false
        
        for (now_login in db) {
            if (flag) {
                break
            }
            
            val now_id = now_login[0]
            val now_pw = now_login[1]
            
            if (now_id == id_pw[0]) {
                if (now_pw == id_pw[1]) {
                    answer = "login"
                    flag = true
                    break
                } else {
                    answer = "wrong pw"
                }
            }
        }
        return answer
    }
}