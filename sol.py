def maxPosPrefixes(arr):
    n = len(arr)
    newArr = []

    arr.sort(reverse=True)

    for i in range(n):
        if i == 0:
            newArr.append(arr[i])
        else:
            sum = arr[i]
            j = i - 1
            if j >= 0:
                sum += newArr[j]
            newArr.append(sum)
    num_pos = 0
    for i in newArr:
        if i > 0:
            num_pos += 1
    return num_pos

# arr = [-6,3,4,-10]
# print(maxPosPrefixes(arr))
# arr = [-3,0,2,1]
# print(maxPosPrefixes(arr))
# arr = [-3,0,-2]
# print(maxPosPrefixes(arr))

# x = [0,2]
# y = [0,4]

# coords = (0,0) and (2,4)
def minArea(x,y,k):
    min_x = x[0]
    max_y = y[0]
    for i,j in zip(x,y):
        if i < min_x:
            min_x = i
        if j > max_y:
            max_y = j
    length = 0

    if max_y > 0:
        length = abs(min_x-1) + abs(max_y+1)
    elif max_y < 0:
        length = abs(min_x-1) + abs(max_y-1)
    
    area = length**2
    return area
    


x = [0,2]
y = [0,4]
k = 2

x = [0,2]
y = [0,7]
k = 2

-7 -2

print(minArea(x,y,k))


















