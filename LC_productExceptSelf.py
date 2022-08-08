def productExceptSelf(nums: list[int]) -> list[int]:
    answer = []

    prefix = [1]
    postfix = deque([1])

    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] * nums[i - 1])

    for i in range(len(nums) - 2, -1, -1):
        postfix.appendleft(postfix[0] * nums[i + 1])

    for i in range(len(nums)):
        answer.append(prefix[i] * postfix[i])

    return answer
