# DAY 1 
## Part 1
1. Sort right and left list in ascending order
2. Loop through each index of left and right, take difference between the two, and add to total
- Time complexity: nlog(n)
- Space complexity: O(1)
## Part 2
1. Create hashmap to store frequencies of ids in right list
2. Loop through ids in left list and check if it exists in hashmap
3. If it exists, add to total the id * frequency
- Time complexity: O(n)
- Space complexity: O(n)

# Day 2
## Part 1
1. Loop through each report in reports
2. Check ascending and descending condition for each report
3. If not strictly ascending or descending or difference is more than 3, add to total
- Time complexity: O(n)
- Space complexity: O(1)
## Part 2
1. Loop through each report in reports
2. Loop through each level in the report
3. Initiate prev variable to store the last seen levels and count variable to count levels that are bad
4. If current levels breaks asc/des rule or difference rule, prev stays the same and increment count. Else, prev equals current level
5. If count >= 2, report is unsafe, dont add to total. Else, add to total
6. Do for both ascending and decending as well as reverse order to account for scenarios where removing first bad level isnt optimal 
- Time complexity: O(n)
- Space complexity: O(1)