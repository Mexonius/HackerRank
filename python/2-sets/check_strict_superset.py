#https://en.wikipedia.org/wiki/Subset
#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(sorted(set(map(int, input().split()))))
n=int(input())

if 0<len(A)<501 and 0<n<21:
    for i in range(n):
        other=set(sorted(set(map(int, input().split()))))
        if not 0<len(other)<101:
            exit()
        for x in other:
            if x not in A:
                print(False)
                exit()
    print(True)
else:
    print(False)