# String s given. Find substring with unique only characters
# return the longest substring


def longestSubstr(s: str):
    unique_chars = set()
    r = 0
    res = ''
    tmp_str = ''

    for l in range(len(s)):
        while r < len(s) and s[r] not in unique_chars:
            unique_chars.add(s[r])
            tmp_str += s[r]
            r += 1
        res = tmp_str if len(tmp_str) > len(res) else res
        unique_chars.remove(s[l])
        tmp_str = tmp_str[1:]
    return res