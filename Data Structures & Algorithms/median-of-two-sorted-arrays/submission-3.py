class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getkth(A, B, k):
            # return the k-th small in merge(A,B)
            if not A:
                return B[k-1]
            if not B:
                return A[k-1]
            if k == 1:
                return min(A[0],B[0])
   

            i = min(len(A), k//2)
            j = min(len(B), k//2)

            if A[i-1] > B[j-1]:
                # drop B[:j]
                return getkth(A,B[j:],k-j)
            else:
                # drop A[:i]
                return getkth(A[i:],B,k-i)
        
        m,n = len(nums1),len(nums2)
        if (m+n) % 2 == 0: # even
            return (getkth(nums1,nums2, (m+n)//2)+getkth(nums1,nums2, (m+n)//2+1))/2
        else:
            return getkth(nums1,nums2, (m+n)//2+1)