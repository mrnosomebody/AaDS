# Sorted array given. Find the closest to the target
# sum of two values and return their indexes

def closestSum(nums, target) -> list:
    r = len(nums) - 1
    l = 0
    prev_sum = 0
    res = [0, r]

    while l < r:
        s = nums[l] + nums[r]
        if abs(target - s) < abs(target - prev_sum):
            res = [l, r]

        if s == target:
            return [l, r]
        elif s > target:
            r -= 1
        else:
            l += 1
        prev_sum = s
    return res

