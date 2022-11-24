# python Q2264_Largest_3-Same-Digit_Number_in_String.py


class Solution(object):
    def largestGoodInteger(self, num):
        len_of_num = len(num)
        result = ""

        # 1.loop all string :
        #   1.1 loop 長度 = len_of_num-2 因為每三個num一數, 總共只要num-2圈即可跑完迴圈
        for i in range(len_of_num-2):
            # 1.2 取出str連續三個值, 迴圈持續往前推進 (ex : 012345 -> 012 123 234 345)
            Part_of_InputString_num = num[i:i+3]

            # 2.確定連續三個數都相同的, 取出來做判斷 :
            #   2.1 利用set 加上 len去判斷讀出來的值是否僅為單一(brilliant !!)
            #   print("set : ", set(Part_of_InputString_num))
            if len(set(Part_of_InputString_num)) == 1:

                # 2.2 比對先前的連續三個數與新進的連續三個數, 選大的
                result = max(result, Part_of_InputString_num)
                print("Final result : ", result)

        return result


obj = Solution()
print(obj.largestGoodInteger("230001922376555934"))

# example1  "6777133339"
# example2  "2300019"
# example3  "42352338"
