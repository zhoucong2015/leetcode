class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        def findKthItem(A, B, k):
            # Find the kth smallest element in the two sorted arrays A and B.
 
            # Swap the arrays A and B if needed. Make sure that A is the non-bigger one.
            # Otherwise, the stepsB might be out of range. For example,
            # A = [2,3,4,5,6,7,8,9,10], B = [1], k = 9, the stepsA would be 4, and stepsB
            # would be 3, if not swapped.
            #
            # ATTENTION: the stepsA might be -1 if len(A) is zero. But it is harmless
            # in the next if-elif-else block.
            if len(A) > len(B):             A, B = B, A
            # stepsA = (endIndex + beginIndex_as_0) / 2
            stepsA = (min(len(A), k) -1)/ 2
            # stepsB =  k - (stepsA + 1) -1 for the 0-based index
            stepsB = k - stepsA - 2
 
            # Only array B contains elements
            if len(A) == 0:                 return B[k-1]
            # Both A and B contain elements, and we need the smallest one
            elif k == 1:                    return min(A[0], B[0])
            # The median would be either A[stepsA] or B[stepsB], while A[stepsA] and 
            # B[stepsB] have the same value.
            elif A[stepsA] == B[stepsB]:    return A[stepsA]
            # The median must be in the right part of B or left part of A
            elif A[stepsA] > B[stepsB]:     return findKthItem(A, B[stepsB+1:], k-stepsB-1)
            # The median must be in the right part of A or left part of B
            else:                           return findKthItem(A[stepsA+1:], B, k-stepsA-1)
 
        # There must be at least one element in these two arrays
        assert not(len(A) == 0 and len(B) == 0)
 
        if (len(A)+len(B))%2==1:
            # There are odd number of elements in total. The median the one in the middle
            return findKthItem(A, B, (len(A)+len(B))/2+1) * 1.0
        else:
            # There are even number of elements in total. The median the mean value of the
            # middle two elements.
            return ( findKthItem(A, B, (len(A)+len(B))/2+1) + 
                     findKthItem(A, B, (len(A)+len(B))/2) ) / 2.0
