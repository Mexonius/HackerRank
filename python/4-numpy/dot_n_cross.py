# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

n = int(input())
# MATRICE ::= Lista di liste
A = [ list(map(int, input().split())) for _ in range(n) ]
B = [ list(map(int, input().split())) for _ in range(n) ]

# numpy.array accetta come paramentro anche una matrice (lista di liste)!!! 
print( numpy.dot(numpy.array(A), numpy.array(B)))

# VERSIONE COMPATTA
# n = int(input())
# A = numpy.array( [ list(map(int, input().split())) for _ in range(n) ] )
# B = numpy.array( [ list(map(int, input().split())) for _ in range(n) ] )
# print( numpy.dot(A,B)
