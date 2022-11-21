# python Q1742_MaximumNumberofBallsinaBox.py


def Sum_of_InputValue(the_value_between_twoInput):
    sum = 0

    # A.regard the input value as string, and add it each by each to become the "final value of summation"(sum)
    for i in str(the_value_between_twoInput):

        # B.add it each by each to become the "final value of summation"(sum)
        sum += int(i)
    return sum


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # create a list to store the value, set the len of list = highLimit + 1
        list_all = [0]*(highLimit-lowLimit+2)

        for i in range(lowLimit, highLimit+1):

            # Add each input(Sum of InputValue) value into the list
            list_all[Sum_of_InputValue(i)] += 1

        print("Final list : ", list_all)
        maximun = max(list_all)
        index = list_all.index(maximun)
        print("The max value's-Index of List is : ", index)
        print("")
        return max(list_all)  # return the max value in the list


obj = Solution()
print(obj.countBalls(1, 10))
print(obj.countBalls(5, 15))
print(obj.countBalls(19, 28))
