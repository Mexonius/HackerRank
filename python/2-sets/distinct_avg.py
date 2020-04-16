# AVG of DISTINCT elements taken from a sequence
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
    s = set(array) # convert the entire array into list in order to discard duplicates
    l = len(s)
    return sum(s)/l

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if 0< n <= 100:
        result = average(arr)
    print(result)