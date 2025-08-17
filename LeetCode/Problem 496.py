class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n =  len(nums2)
        res = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if len(stack) != 0:
                res[i] = stack[-1]
            stack.append(nums2[i])
        ans = []
        for i in range(len(nums1)):
            ans.append(res[nums2.index(nums1[i])])
        return ans