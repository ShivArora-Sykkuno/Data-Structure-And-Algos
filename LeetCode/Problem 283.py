class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        freq = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                freq +=1
            else:
                temp.append(nums[i])

        for i in range(freq):
            temp.append(0)
        
        nums[:] = temp[:]