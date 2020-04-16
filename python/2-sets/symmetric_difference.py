# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
#Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
n = int(input())
en = set(map(int, input().split()))
b = int(input())
fr = set(map(int, input().split()))
print(len(en ^ fr)) # ^ works as symmetric_difference() ONLY between two sets