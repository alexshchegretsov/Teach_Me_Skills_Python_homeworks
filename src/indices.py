nums = [3, 3]
# nums = [3, 2, 4]
target = 6
indices = []
length = len(nums)
i = 0
# while i < length:
#
#     for x in range(i+1,length):
#         if nums[i] + nums[x] == target:
#             indices.append(i)
#             indices.append(x)
#     i += 1
# print(indices)
while i < length:
    if (target - nums[i]) in nums[i+1:]:
        a_1 = nums.index(target-nums[i])
        indices.append(i)
        indices.append(a_1)
    i += 1
print(indices)