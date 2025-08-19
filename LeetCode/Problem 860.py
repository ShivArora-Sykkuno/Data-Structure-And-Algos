class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        # twenty = 0  --- This is not needed in this solution but if asked for total amount you have then ----
        for bill in bills:
            if bill == 5:
                five +=1
            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                    # twenty += 1
                elif five >= 3:
                    five -=3
                    # twenty += 1
                else:
                    return False
        return True 