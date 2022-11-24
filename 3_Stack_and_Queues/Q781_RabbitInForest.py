# python Q781_RabbitInForest.py
# python collection.counter : https://blog.csdn.net/sinat_28576553/article/details/99131954
# 題目理解 : https://www.youtube.com/watch?v=taPpHtgVLhw

from collections import Counter


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        func_counter = Counter()
        res = 0

        # (!)variable "answers" is a list, so i is the value of list instaed of index(順序值)
        for i in answers:

            # 這邊的操作是將第一隻兔子的數量加上第一隻兔子除第二隻數量的餘數, 以次類推疊加加上去
            if func_counter[i] % (i + 1) == 0:
                # print(i)
                res += i + 1
                print(res)
            func_counter[i] += 1

        return res


answers = [1, 2, 4]  # (1+1) + (2+1)
# answers = [10, 10, 10] # (10+1) 三隻有可能同色不同隻看出去都是10隻
obj = Solution()
print(obj.numRabbits(answers))
