# list=[1,1,2,2,3,3]
# rslt=[]
# for i in list:
#     if i not in rslt: 
#         rslt.append(i)
# print(rslt)

# def d():
#     digits=[1,1,5]
#     n = len(digits)
#     for i in range(n - 1, -1, -1):
#         digits[i] += 1
#         digits[i] %= 10
#         if digits[i] != 0:
#             return digits
#         return [1] + digits
# print(d())

# nums1=[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3
# for j in range(n):
#     nums1[j+m]=nums2[j]
# nums1.sort()
# print(nums1)

nums=[1,1,2]
for i in range(len(nums)):
    for j in range(1,len(nums)):
        if nums[i]==nums[j]:
            nums.remove(nums[i])
            nums.append("-")
print(nums)