# nums = [3,2,2,3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
# val = 2
# if not len(nums):
#     pass    # return 0
# for j in range(0, len(nums)-1):
#     if nums[j+1] != val:
#         nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)
#


# if not len(nums):
#     pass
# i = 0
# length = len(nums)
# for j in range(1, length):
#     if nums[j] != nums[i]:
#         i += 1
#         nums[j], nums[i] = nums[i], nums[j]
#
# print(nums)


s = 'abba'
t = 'odod'
count = 0

for i in range(len(s)-1):
    if s.count(s[i]) == t.count(t[i]) and (ord(s[i]-ord(s[i+1])))

# for i,x in enumerate(s):
#     if s.count(x) == t.count(t[i]):
#         count += 1
# print(count == len(s))



