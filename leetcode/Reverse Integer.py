class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:   return int(str(x)[1:][::-1])*-1
        else:       return int(str(x)[::-1])

class Solution:
    # @return an integer
    def _reverse_helper(self, x):
        if -10 < x < 10:
            return x, 1
        else:
            rest, digits = self._reverse_helper(x / 10)
            return x % 10 * (10 ** digits) + rest, digits + 1
 
    def reverse(self, x):
        if x < 0:   return self._reverse_helper(-x)[0] * -1
        else:       return self._reverse_helper(x)[0]

class Solution:
    # @return an integer
    def _reverse_helper(self, x):
        if -10 < x < 10:
            return x, 1
        else:
            rest, digits = self._reverse_helper(x / 10)
            return x % 10 * (10 ** digits) + rest, digits + 1
 
    def reverse(self, x):
        if x < 0:   result = self._reverse_helper(-x)[0] * -1
        else:       result = self._reverse_helper(x)[0]
        
        if -2147483648L <= result <= 2147483647L:   return result
        else:                                       return 0
