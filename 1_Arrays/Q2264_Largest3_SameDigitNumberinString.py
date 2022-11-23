# python Q2264_Largest3_SameDigitNumberinString.py


class Solution:
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)
        result = ""

        # 這邊-2 是因為一次取三個值, 所以迴圈次數可以少兩次, 如果一次取N個值這個數為N-2
        for i in range(n-2):

            # continue 3-digit in number(num)
            continue3 = num[i:i+3]

            # 利用set技巧, 找出連續三個數值皆為相同值的方法, 再用比較方法選出最大值, 儲存最大值成為答案
            if len(set(continue3)) == 1:
                result = max(result, continue3)
                # print(result)
        return result


# num = "6777133339"  # Output: "777"
# num = "2300019"  # Output: "000"
# num = "42352338"  # Output: ""

num = "00012344456677789991111"
obj = Solution()
print(obj.largestGoodInteger(num))
