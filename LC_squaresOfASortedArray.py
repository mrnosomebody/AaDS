def sortedSquares(nums: list[int]) -> List[int]:
    size = len(nums)
    l = 0
    r = size - 1
    sq_left = 0
    sq_right = nums[-1] * nums[-1]
    res = deque()

    while l <= r:
        sq_left = nums[l] * nums[l]
        while sq_right > sq_left:
            res.appendleft(sq_right)
            r -= 1
            sq_right = nums[r] * nums[r]
        res.appendleft(sq_left)
        l += 1
    return res