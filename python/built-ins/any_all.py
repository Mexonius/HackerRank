# https://www.hackerrank.com/challenges/any-or-all/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT

# # "LONG SOLUTION"
# n,arr=int(input()),list(map(str, input().split()))
# if all([int(x)>0 for x in arr]) and any([True for x in arr for i in range(len(x)) if x[i]==x[len(x)-i-1]]):
#     print(True)
# else:
#     print(False)

# # "3-LINE SOLUTION"
# n,arr=int(input()),list(map(str, input().split()))
# evaluation = True if all([int(x)>0 for x in arr]) and any([True for x in arr for i in range(len(x)) if x[i]==x[len(x)-i-1]]) else False
# print(evaluation)

# "2-LINE SOLUTION"
n,arr=int(input()),list(map(str, input().split()))
print(True if all([int(x)>0 for x in arr]) and any([True for x in arr for i in range(len(x)) if x[i]==x[len(x)-i-1]]) else False)