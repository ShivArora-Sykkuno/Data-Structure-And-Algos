class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = m
        for i in range(n):
            nums1[temp] = nums2[i]
            temp += 1
        nums1.sort()
        print(nums1)