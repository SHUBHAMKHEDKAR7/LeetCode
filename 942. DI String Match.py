class Solution:
    def diStringMatch(self, s):
        n = len(s)

        low = 0
        high = n

        perm = []

        for ch in s:
            if ch == 'I':
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1

        # Add the last remaining number
        perm.append(low)

        return perm