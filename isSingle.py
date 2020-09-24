def singleNumber(nums):
        """
        a xor 0 = a
        a xor a = 0
        """
        a = 0
        for i in nums:
            a ^= i
        return a