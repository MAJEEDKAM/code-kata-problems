import statistics

n = input()
arr = list(map(int, input().split()))
arr.sort()
print(statistics.median(arr))
