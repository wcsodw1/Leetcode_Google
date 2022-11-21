# python Q1_TwoSum.py


class Solution:
    def effectivy_twosum(self, nums_of_list, target):
        print("Target is :", target)
        HashMap = dict()  # create a blank dict, to append the order of target related value

        # 1.get target by arithmatic:
        for i in range(len(nums_of_list)):
            num = nums_of_list[i]  # change variable name
            sub = target - num
            #print(num, sub)

            # 2.put the order in the list :
            if num in HashMap:
                print("與num相對的值", num)
                # dict_Map[num] == the order of 'dict_Map'
                # i == 下一個相加會等於target的值在貞烈中的順序(等於是直接放入順序進去)
                return [HashMap[num], i]
            else:
                HashMap[sub] = i  # dict中sub值在裡面的順序

    def david_force_twosum(self, nums_of_list, target):
        print("Hi Leetcode, Nice to meet you!")

        print("# 1.迴圈設計-兩個迴圈可將同一個陣列的所有值去互動(相加 相乘...等等)")
        print("# 2.用迴圈跑並print出陣列中所有2個數值去相加的可能性")

        for i in range(len(nums_of_list)):
            for j in range(i+1, len(nums_of_list)):  # 1.i+1 represent j迴圈將從i迴圈的遞增一個值作為開始
                sum = nums_of_list[i]+nums_of_list[j]

                # 2.用迴圈跑並print出陣列中所有2個數值去相加的可能性
                #print("list中的[i][j]相加值", i, j, ":", sum)

                # 3.如果相加值與設定的目標相同, 帶入條件式裡做第二階段的運算
                if sum == target:
                    print("target '", target, "' = i 的第",
                          i, "個", "加 j 的第", j, "個的相加")
                    # print("Target Sum is", sum)
                    # print("Index i is :", i)
                    # print("Index j is :", j)
                    # 4.return 回傳以便(object)物件使用
                    return[i, j]

    # The same logic with above
    def twoSum(self, nums, target):
        print("Hi Leetcode, Nice to meet you!")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i]+nums[j]
                #print("sum", sum)
                if sum == target:
                    print("Target Sum is", sum)
                    print("Index i is :", i)
                    print("Index j is :", j)

                    return [i, j]



# Use the object : 
object_ = Solution()
list1 = [2, 7, 11, 15]
target = 18
print(object_.effectivy_twosum(list1, target))
