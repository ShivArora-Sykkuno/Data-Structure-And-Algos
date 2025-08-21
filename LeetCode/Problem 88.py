class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j =0
        while j < n:
            if i < m and nums2[j] < nums1[i]:
                for k in range(m, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                i += 1
                j += 1
                m += 1 
            elif i >= m: 
                nums1[i] = nums2[j]
                i += 1
                j += 1
            else:
                i+=1

        