class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        mat2flat = lambda x,y : x*n+y
        flat2mat = lambda idx : (idx // n,idx % n)

        l = 0
        r = m*n-1

        while l<=r:
            # include both l and r 
            mid = l + ((r-l)//2)
            i,j = flat2mat(mid)
            mat_mid = matrix[i][j]
            if mat_mid == target:
                return True
            if mat_mid > target:
                r = mid-1
            elif mat_mid < target:
                l = mid+1
        
        return False
            

