fun main(args: Array<String>) {
    val s1 = readLine()!!
    var answer = StringBuilder()
    
    for (s in s1) {
        answer.append(when {
            s.isUpperCase() -> s.toLowerCase()
            else -> s.toUpperCase()
        })
    }
    
    println(answer.toString())
}