import (
    "strconv"
)

func solution(s string) int {
    if s[0] == '-' {
        n, _ := strconv.Atoi(s[1:])
        return -n
    }

    n, _ := strconv.Atoi(s)
    return n
}