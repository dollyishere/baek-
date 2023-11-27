import java.lang.Math.abs

class Solution {
    fun solution(a: Int, b: Int, c: Int, d: Int): Int {
        var answer: Int = 0
        var totalArray: IntArray = IntArray(7){0}
        
        totalArray[a] ++
        totalArray[b] ++
        totalArray[c] ++
        totalArray[d] ++
        
        var maxV = totalArray.maxOrNull()
        
        when(maxV) {
            4 -> answer = 1111 * a
            3 -> {
                var p = totalArray.indexOf(3)
                var q = totalArray.indexOf(1)
                answer = ((10*p)+q) * ((10*p)+q)
            }
            2 -> {
                var p = 0
                var q = 0
                var r = 0
                for (i in 1 until totalArray.size) {
                    if (totalArray[i] == 2) {
                        if (p == 0) {
                            p = i
                        } else {
                            q = i
                        }
                    } else if (totalArray[i] == 1) {
                        if (q == 0) {
                            q = i
                        } else {
                            r = i
                        }
                    }
                }

                if (r != 0) {
                    answer = q * r
                } else {
                    answer = (p + q) * abs(p-q)
                }
            }
            else -> {
                    for (i in 0 until totalArray.size) {
                    if (totalArray[i] >= 1) {
                        answer = i
                        break
                    }
                }
            }
        }
        
        return answer
    }
}