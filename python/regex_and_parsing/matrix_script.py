# https://www.hackerrank.com/challenges/matrix-script/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

# TODO  Nel programma non si devono utilizzare gli if di cristo....
#       sicuro bisogna usa le cazzo di espressioni regolari...


# def isalphanum(c):
#     alphanum = [range(ord('a'), ord('z')), range(ord('A'), ord('Z')), range(ord('0'), ord('9'))]
#     return any([(True if ord(c) in r else False) for r in alphanum ])


# n,m= [int(x) for x in input().split()]
# matrix_enc=[input() for _ in range(n)]
# string= "".join([ x[j] for j in range(m) for x in matrix_enc ])

# start,i=0,1
# while(i<len(string)):
#     if isalphanum(string[i-1]) and not isalphanum(string[i]):
#         start=i
#     elif not isalphanum(string[i-1]) and isalphanum(string[i]):
#         string=string.replace(string[start:i], ' ')
#         i=start+1
#     i+=1

# print(string)



n,m= [int(x) for x in input().split()]
matrix_enc=[input() for _ in range(n)]
string= "".join([ x[j] for j in range(m) for x in matrix_enc ])



print(string)