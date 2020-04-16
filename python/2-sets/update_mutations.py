# https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
A = set(map(int, input().split()))
n = int(input())
command=set()
for i in range(n):
    command = input().split()
    if command[0] == 'update': # or |=
        otherset=set(map(int, input().split()))
        A|=otherset
    elif command[0] == 'intersection_update': # or &=
        otherset=set(map(int, input().split()))
        A&=otherset
    elif command[0] == 'difference_update': # or -=
        otherset=set(map(int, input().split()))
        A-=otherset
    elif command[0] == 'symmetric_difference_update': # or ^=
        otherset=set(map(int, input().split()))
        A^=otherset

print( sum(A) )