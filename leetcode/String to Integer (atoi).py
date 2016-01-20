class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX, INT_MIN = 2147483647, -2147483648
        index = 0
        result = 0
        sign = 1        # Default we are processing a non-negative number
 
        if len(str) == 0:   return 0    # The result for empty string is 0.
 
        while str[index].isspace():     index += 1  # Discard whitespace
 
        if str[index] == "-":           sign = -1
        if str[index] in "-+":          index += 1  # Discard sign char
 
        while index < len(str) and str[index].isdigit():
            result = result * 10 + (ord(str[index]) - ord("0")) * sign
            index += 1
 
            # Handle overflow. Because Python could handle the large
            # integer, this code works well. If with C/C++, we should use
            # another method. For example, with non-negative number, the
            # test condition for overflow would be:
            # if( INT_MAX / 10 < result || INT_MAX - result * 10 < 
            #    (ord(str[index]) - ord("0")) )
            if sign == 1 and result >= INT_MAX:     return INT_MAX
            elif sign == -1 and result <= INT_MIN:  return INT_MIN
 
        return result
