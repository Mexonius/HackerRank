#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n = int(input())
en = set(map(int, input().split()))
b = int(input())
fr = set(map(int, input().split()))
print(len(en - fr)) # - works as difference() ONLY between two sets