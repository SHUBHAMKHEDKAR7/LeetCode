class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left , right + 1):
            is_valid = True
            for digit in str(num) :
                d = int(digit)

                if d == 0:
                    is_valid = False
                    break
                if num % d != 0:
                    is_valid = False
            if is_valid:
                result.append(num)

        return result 
