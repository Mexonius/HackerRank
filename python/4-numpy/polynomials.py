# https://www.hackerrank.com/challenges/np-polynomials/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import numpy

poly_coef = list(map(float, input().split()))
poly_coef.reverse()
x = int(input())

# l=[]
# for i in range(len(poly_coef)):
#     l.append(poly_coef[i] * x**i)

value = sum([poly_coef[i]*x**i for i in range(len(poly_coef))])
print(value)
