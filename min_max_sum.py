def miniMaxSum(arr):
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print("{} {}".format(min_sum,max_sum))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
