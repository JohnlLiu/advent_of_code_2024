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

# Day 3
## Part 1
1. Parse using regex to get all occurances of 'mul(x,y)'
2. For each occurance of 'mul(x,y)', parse using regex again to find just x and y
3. Multiply x and y and add to total
- Time complexity: O(n)
- Space complexity: O(n)
## Part 2
1. Parse using regex to get all occurances of 'mul(x,y)', 'don't()', and 'do()'
2. Use a bool 'do' to keep track of whether or not multiply
3. Loop through each found regex match, if 'don't()' then do = False, elif 'do()' then do = True
4. For each occurance of 'mul(x,y)', parse using regex again to find just x and y
5. If do == True, multiply x and y and add 1 to total
- Time complexity: O(n)
- Space complexity: O(n)

# Day 4
## Part 1
1. Treat input as a grid
2. Loop through each cell in the grid and check if cell is 'X'
3. For each cell that is 'X', check in the 8 directions from that cell to see if it can make 'XMAS'
4. For each direction that can make 'XMAS', add 1 to result
- Time complexity: O(n) where n is total number of characters in the grid 
- Space complexity: O(1)
## Part 2
1. Loop through each cell ignoring edge cells since they cant be middle of a X-MAS and check if cell is 'A'
2. For each cell that is 'A', check opposite corner pairs if 1 is 'M' and the other is 'S'
3. For each cell where the 4 corners and their opposite corner satisfies the condition, add 1 to total
- Time complexity: O(n) where n is total number of characters in the grid 
- Space complexity: O(1)