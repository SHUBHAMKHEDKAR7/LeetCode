class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        for op in operations :
            if op == "C":
                score.pop()
            elif op == "D":
                score.append(2 * score[-1])
            elif op == "+":
                score.append(score[-2] + score[-1])
            else:
                score.append(int(op))
        return sum(score)