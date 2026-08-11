class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {}

        # Store index of each string in list1
        for i in range(len(list1)):
            index_map[list1[i]] = i

        min_sum = float('inf')
        answer = []

        # Check strings in list2
        for j in range(len(list2)):
            word = list2[j]

            if word in index_map:
                index_sum = index_map[word] + j

                if index_sum < min_sum:
                    min_sum = index_sum
                    answer = [word]

                elif index_sum == min_sum:
                    answer.append(word)

        return answer