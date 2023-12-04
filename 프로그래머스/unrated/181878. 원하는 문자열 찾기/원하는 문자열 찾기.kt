class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        var tempS: String = ""
  
        if (pat.length <= myString.length) {
            for (i in 0 until myString.length) {
                tempS += myString[i].toString()
                
                if (tempS.length == pat.length) {              
                    if (tempS.equals(pat, ignoreCase = true)) {
                        answer ++
                        break
                    } else {
                        tempS = tempS.slice(1 until tempS.length)
                    }
                }
            }
        }
        
        return answer
    }
}