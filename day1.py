with open('day1.txt') as f: s = f.readlines()
nums1 = []
nums2 = []
for x in s:
        nums1.append(int(x.split('   ')[0]))
        nums2.append(int(x.split('   ')[1].rstrip()))

def day1_part1(nums1, nums2):
    res = 0
    nums1.sort()
    nums2.sort()

    for i in range(len(nums1)):
          res += abs(nums1[i] - nums2[i])
    
    return res

def day1_part2(nums1, nums2):
    res = 0
    counts = {}

    for i in range(len(nums1)):
        right = nums2[i]
        if right in counts:
             counts[right] += 1
        else:
             counts[right] = 1
    
    for num in nums1:
         if num in counts:
              res += (num * counts[num])
    
    return res

print(day1_part1(nums1, nums2))
print(day1_part2(nums1, nums2))
    

