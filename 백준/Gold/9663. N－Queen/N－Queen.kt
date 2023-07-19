import java.util.*
import kotlin.math.abs

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    var answer : Int = 0
    var chessBoard = IntArray(n)

    fun promising(i : Int) : Boolean {
        for (k in 0 until i.coerceAtLeast(0)) {
            if ((chessBoard[i] == chessBoard[k]) || (abs(chessBoard[i] - chessBoard[k]) == abs(i-k))) {
                return false
            }
        }
        return true
    }

    fun backTrack(i: Int) {
        if (i == n) {
            answer++
            return
        } else {
            for (j in 0 until n) {
                chessBoard[i] = j
                if (promising(i)) {
                    backTrack(i+1)
                }
            }
        }
    }

    backTrack(0)
    println(answer)
}
