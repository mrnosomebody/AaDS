def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    l = 0
    zeroes = 0

    for r in range(0, length):
        if nums[r] == 0:
            zeroes += 1
        else:
            nums[l] = nums[r]
            l += 1
    for i in range(length - zeroes, length):
        nums[i] = 0