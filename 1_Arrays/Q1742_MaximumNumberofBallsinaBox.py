# python Q1742_MaximumNumberofBallsinaBox.py


def Sum_of_InputValue(the_value_between_twoInput):
    sum = 0

    # A.regard the input value as string, and add it each by each to become the "final value of summation"(sum)
    for i in str(the_value_between_twoInput):

        # B.add it each by each to become the "final value of summation"(sum)
        #print("i :", i)
        sum += int(i)
        #print("sum", sum)
    return sum


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        # 1.create a list with all 0, to store the value, set the len of list = highLimit + 1
        list_all = [0]*(highLimit-lowLimit+2)

        # 2.loop from parameter1 to parameter2 :
        for i in range(lowLimit, highLimit+1):

            # 2.1 Add each input(Sum of InputValue) value into the list
            list_all[Sum_of_InputValue(i)] += 1

        print("Final list : ", list_all)
        maximun = max(list_all)
        index = list_all.index(maximun)

        # optional(max value)
        print("The max value's-Index of List is : ", index)
        # print("")

        # return the counting of index with max-value in the list(回傳list中index最多值的數量)
        return max(list_all)


obj = Solution()
print(obj.countBalls(1, 10))
print(obj.countBalls(5, 15))
print(obj.countBalls(19, 28))
