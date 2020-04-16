# https://www.hackerrank.com/challenges/security-inverse-of-a-function/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
codomain = list(map(int, input().split()))

if 1<=n<=20 and max(codomain)==n:
    domain = [0]*n
    for x in range(n):
        domain[ codomain[x] - 1 ] = x+1

    for i in range(n):
        print(domain[i])