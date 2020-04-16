# https://www.hackerrank.com/challenges/security-tutorial-permutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
codomain = list(map(int, input().split()))

if 1<=n<=20 and max(codomain)==n:
    for x in codomain:
        print(codomain[x-1])