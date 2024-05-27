import heapq

def topKFrequent(nums, k):
    if len(nums) == k :
        return nums
    map={}
    for i in nums:
        if i not in map.keys():
            map[i] = 1
        else:
            map[i] += 1
    print(heapq.nlargest(k,map.keys(),key=map.get))

if __name__ == '__main__':
    topKFrequent([4,1,-1,2,-1,2,3], 2)
