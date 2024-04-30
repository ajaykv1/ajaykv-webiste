from queue import Queue
# # Complete the 'reachTheEnd' function below. # 
# # The function is expected to return a STRING. 
# # The function accepts following parameters: 
# #  1. STRING_ARRAY grid #  2. INTEGER maxTime 
# # 
def reachTheEnd(grid, maxTime): 

    checked = []
    steps = []
    for r in range(len(grid)):
        checked.append([])
        for c in range(len(grid[0])):
            checked[r].append(False)

    queue = Queue() 
    queue.put((0, 0, 0))

    while queue.empty() == False: 
        location = queue.get() 
        row = location[0]
        col = location[1] 

        up_one_pos = row - 1
        down_one_pos = row + 1
        right_one_pos = col + 1
        left_one_pos = col - 1

        checked[row][col] = True

        if row < len(grid) - 1 and col < len(grid[0]) - 1: 

            if grid[down_one_pos][col] == '.' and checked[down_one_pos][col] == False: 
                queue.put((down_one_pos, col, location[2] + 1)) 

            if grid[row][right_one_pos] == '.' and checked[row][right_one_pos] == False: 
                queue.put((row, right_one_pos, location[2] + 1)) 

        elif row < len(grid) - 1 and grid[down_one_pos][col] == '.' and checked[down_one_pos][col] == False:
            queue.put((down_one_pos, col, location[2] + 1)) 

        elif col < len(grid[0]) - 1 and grid[row][right_one_pos] == '.' and checked[row][right_one_pos] == False: 
            queue.put((row, right_one_pos, location[2] + 1)) 

        if row > 0 and col > 0: 

            if grid[up_one_pos][col] == '.' and checked[up_one_pos][col] == False: 
                queue.put((up_one_pos, col, location[2] + 1))
            
            if grid[row][left_one_pos - 1] == '.' and checked[row][left_one_pos] == False: 
                queue.put((row, left_one_pos, location[2] + 1)) 

        elif row > 0 and grid[up_one_pos][col] == '.' and checked[up_one_pos][col] == False:
            queue.put((up_one_pos, col, location[2] + 1)) 

        elif col > 0 and grid[row][left_one_pos] == '.' and checked[row][left_one_pos] == False:
            queue.put((row, left_one_pos, location[2] + 1)) 


        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            steps.append(location[2])
    
    if len(steps) == 0:
        return False
    minimum = max(steps)
    for i in steps:
        if i < minimum:
            minimum = i

    if minimum <= maxTime:
        return True
    else:
        return False

grid = ["..##", "#.##", "#..."]
maxTime = 5
print(steps)
# grid = [".#","#."]
# maxTime = 2

print(reachTheEnd(grid, maxTime))











