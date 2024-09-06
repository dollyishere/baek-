class Solution {
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        var answer: String = ""
        val initialTime = updatedTimeFromString(pos)
        val endTime = updatedTimeFromString(video_len)

        val time = Time(initialTime.minute, initialTime.second)
        
        opening_skip(time, op_start, op_end)
        
        for (command in commands) {
            // println(formatTime(time))
            when {
                command == "prev" -> {
                    time.second -= 10
                    if (time.second < 0) {
                        time.minute--
                        time.second += 60
                    }
                    if (time.minute < 0) {
                        time.minute = 0
                        time.second = 0
                    }
                }
                else -> {
                    time.second += 10
                    if (time.second >= 60) {
                        time.minute ++
                        time.second -= 60
                    }
                    
                    if (time.minute > endTime.minute || (time.minute == endTime.minute && time.second > endTime.second)) {
                        time.minute = endTime.minute
                        time.second = endTime.second
                    }
                }
            }
            
            opening_skip(time, op_start, op_end)
        }
        
        
        answer = formatTime(time)
        return answer
    }
    
    private fun formatTime(time: Time): String {
        val minuteStr = time.minute.toString().padStart(2, '0')
        val secondStr = time.second.toString().padStart(2, '0')
        
        return "$minuteStr:$secondStr"
    }
    
    fun opening_skip(time: Time, op_start: String, op_end: String) {
        var now_time_f = (time.minute.toString() + "." + time.second.toString().padStart(2, '0')).toFloat()
        
        val op_start_f = (op_start.substring(0..1) + "." + op_start.substring(3..4)).toFloat()
        val op_end_f = (op_end.substring(0..1) + "." + op_end.substring(3..4)).toFloat()

        if (op_start_f <= now_time_f && now_time_f <= op_end_f) {
            time.minute = op_end.substring(0..1).toInt()
            time.second = op_end.substring(3..4).toInt()
        }
    }
}

class Time(var minute: Int, var second: Int)

fun updatedTimeFromString(time_string: String) : Time {
    var minute = time_string.substring(0..1).toInt()
    var second = time_string.substring(3..4).toInt()
    
    return Time(minute, second)
}