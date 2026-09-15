class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        common = {}

        # Count characters of first word
        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1

        # Compare with remaining words
        for word in words[1:]:
            current = {}

            for ch in word:
                current[ch] = current.get(ch, 0) + 1

            for ch in list(common.keys()):
                if ch in current:
                    common[ch] = min(common[ch], current[ch])
                else:
                    common[ch] = 0

        # Create answer
        result = []

        for ch in common:
            for i in range(common[ch]):
                result.append(ch)

        return result