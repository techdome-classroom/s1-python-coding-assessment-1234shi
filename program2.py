def decode_message( s: str, p: str) -> bool:

# write your code here
def isMatch(message, pattern):
    m, n = len(message), len(pattern)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

# Example usage:
message1 = "aa"
pattern1 = "a"
print(isMatch(message1, pattern1))  # Output: False

message2 = "aa"
pattern2 = "*"
print(isMatch(message2, pattern2))  # Output: True

message3 = "cb"
pattern3 = "?a"
print(isMatch(message3, pattern3))  # Output: False

  
        return False
