#brute force solution
def maxArea(height):
    print(height)
    l = 0
    r = len(height)-1
    area = 0
    for i in range(0, r):
        for j in range(r , -1 ,-1):
            max_value = min(height[i],height[j])
            if (max_value * (j-i)) > area:
                area = (max_value * (j - i))
    print(area)

#optimal solution:


if __name__ == '__main__':
    maxArea([4,3,2,1,4])
    maxArea([1,8,6,2,5,4,8,3,7])