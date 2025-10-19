from collections import deque

class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = deque()
        top = -1

        if len(nums) == k:
            return "0"

        for i in range(len(nums)):
            while k > 0 and len(stack) > 0 and stack[-1] > nums[i]:
                stack.pop()
                k -= 1
                top -= 1

            stack.append(nums[i])
            top += 1

        while k > 0 and len(stack) > 0:
            stack.pop()
            k -= 1
            top -= 1

        while len(stack) > 0 and stack[0] == "0":
            stack.popleft()

        if len(stack) == 0:
            return "0"

        return "".join(stack)
