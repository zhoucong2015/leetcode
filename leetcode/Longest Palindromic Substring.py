class Solution:
    # @return a string
    def longestPalindrome(self, s):
        center, right = 0,1
        newS = "#"+"#".join(s)+"#"
        palHalfLenCenteringHere = [1] * len(newS)
 
        for index in xrange(1, len(newS)):
            assert index <= right
            if index < right and index + palHalfLenCenteringHere[2*center-index] < right:
                # No way to extend the right. Thus the center is not changed.
                palHalfLenCenteringHere[index] = palHalfLenCenteringHere[2*center-index]
            else:
                # We MIGHT extend the right. And we DO change the center here.
                # IF we did NOT extend the right, the new center and old one have completely
                # the SAME effect on the next steps/rounds.
                center = index
                if index < right:
                    # Use some pre-computed information
                    palHalfLenCenteringHere[index] = right - center
                else:
                    # Actually scanning from scratch
                    palHalfLenCenteringHere[index] = 1
                    right += 1
 
                # Try to extend the right
                while right < len(newS) and 2*center-right >= 0 and 
                      newS[right] == newS[2*center-right]:
                    right += 1
                    palHalfLenCenteringHere[index] += 1
 
        # Find the longest palindromic substring
        center, halfLen = max(enumerate(palHalfLenCenteringHere), key=lambda x: x[1])
        result = newS[center - halfLen + 1: center + halfLen]
 
        return result.replace("#", "")
