def maxArea(height: list[int]) -> int:
    max_height = max(height)
    res = 0
    l = 0
    r = len(height) - 1

    while l < r:
        res = max(res, (r - l) * min(height[l], height[r]))
        if height[l] == max_height and height[r] == max_height:
            return res

        if height[l] < max_height and height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res