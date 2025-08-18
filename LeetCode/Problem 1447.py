class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n):
            for j in range(i+1,n+1):
                if gcd(j,i)==1:
                    res.append(f'{i}/{j}')
        return res