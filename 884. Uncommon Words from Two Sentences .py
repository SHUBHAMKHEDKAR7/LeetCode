class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        count = {}

        words = s1.split() + s2.split()

        for word in words :
            count[word] = count.get(word , 0) + 1
        answer = []

        for word in count:
            if count[word] == 1:
                answer.append(word)
        return answer