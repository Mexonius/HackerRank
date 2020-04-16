# https://www.hackerrank.com/challenges/zipped/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# https://www.geeksforgeeks.org/input-multiple-values-user-one-line-python/

# Enter your code here. Read input from STDIN. Print output to STDOUT

N,X=[int(x) for x in input().split() ]
table=[list(map(float, input().split())) for _ in range(X)]

avgs=[]
if 0<N<=100 and 0<X<=100:
    for i in range(N):
        avgs.append( [table[s][i] for s in range(X)] )

    final=[ x/X for x in  map(sum, avgs) ]
    for i in final:
        print(i)
