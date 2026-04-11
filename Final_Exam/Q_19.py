def next_greater_to_right(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    stack = []  # store indices

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
