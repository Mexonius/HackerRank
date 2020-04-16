# https://www.hackerrank.com/challenges/np-linear-algebra/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

    # TEST CASE #1
    # INPUT:
    # 1.1 1.1
    # 1.1 1.2
    # OUTPUT:
    # 0.11

    # TEST CASE #0
    # 1.1 1.1
    # 1.1 1.1
    # OUTPUT:
    # 0.0

import numpy

n=int(input())
A=[ list(map(float, input().split())) for _ in range(n)]

det = numpy.linalg.det(A)

# print( '%.2f' % det) # se uso questo test0 e test2 non passano...
# print(det) # se uso questo test1 non passa...

# con 1 cifra decimale passano test2 e test0, se ne metto due passa solo test1 xD

# bastava solo fare round(...) ...
print( round(det,2) )

# spiegazione (possibile)
# con round pensa lui ad arrotondare il valore, invece usando %.2f diciamo che sei tu a FORZARE la VISUALIZZAZIONE 