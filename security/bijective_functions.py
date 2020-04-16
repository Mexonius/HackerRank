#https://www.hackerrank.com/challenges/security-bijective-functions/problem?h_r=next-challenge&h_v=zen

# A strange test case, according to the test of the task
    # INPUT
    # 20
    # 20 19 18 17 16 15 14 13 12 11 1 2 3 4 5 6 7 8 9 10
    # OUTPUT:
    # YES
#  So the problem it's reduced to check if there are in the sequence ALL the number
#  between 1 and n ??

# ACCORDING TO THE STRANGE TEST CASE: I'VE BUILD A SORT OF BLOOM FILTER
n = int(input())
seq = list(map(int, input().split()))

if 1<=n<=20 and max(seq)==n:
    right=[0]*n
    # bloomfilter-like behaviour
    for x in seq:
        if right[x-1]==0:
            right[x-1]=1
        else:
            print("NO")
            exit()
    
print("YES")

# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# seq = list(map(int, input().split()))

# if 1<=n<=20 and max(seq)==n:
#     prev=0
#     for x in seq:
#         if prev!=int(x-1):
#             print("NO")
#             exit()
#         else:
#             prev=x
# else: 
#     print("NO")
#     exit()
    
# print("YES")


