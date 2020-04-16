# https://www.hackerrank.com/challenges/py-set-union/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
en = set(map(int, input().split()))
b = int(input())
fr = set(map(int, input().split()))
print(len(en | fr)) # pipe works as union() ONLY between two sets