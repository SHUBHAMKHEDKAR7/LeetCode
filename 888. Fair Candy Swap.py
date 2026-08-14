class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        difference = (alice_total - bob_total) / 2 
        alice_set = set(aliceSizes) 

        for y in bobSizes:
            x = y + difference
            if x in alice_set:
                return[x , y]