# https://www.hackerrank.com/challenges/security-involution/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
codomain = list(map(int, input().split()))

if 1<=n<=20 and max(codomain)==n:

    # Explanation:
    # the INDEX of codomain (so the value in the domain)
    # must be equal to the position in the array pointed to
    # codomain[index], so
    # index = codomain[ codomain[index] ]

    # Eg #1
    # +----------------+---+---+---+---+---+---+---+
    # | Codomain value | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    # +----------------+---+---+---+---+---+---+---+
    # | Domain value   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    # +----------------+---+---+---+---+---+---+---+
    # | array's index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
    # +----------------+---+---+---+---+---+---+---+

    # Eg #2
    # +----------------+---+---+---+---+---+---+---+
    # | Codomain value | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    # +----------------+---+---+---+---+---+---+---+
    # | Domain value   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    # +----------------+---+---+---+---+---+---+---+
    # | array's index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
    # +----------------+---+---+---+---+---+---+---+

    # Eg #3 (invented by me)
    # +----------------+---+---+---+---+---+---+---+---+
    # | Codomain value | 7 | 4 | 3 | 2 | 8 | 6 | 1 | 5 |
    # +----------------+---+---+---+---+---+---+---+---+
    # | Domain value   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
    # +----------------+---+---+---+---+---+---+---+---+
    # | array's index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    # +----------------+---+---+---+---+---+---+---+---+

    # tables done at: https://ozh.github.io/ascii-tables/

    for x in range(n):
        # print( x, codomain[ codomain[x] -1])
       if (x+1) != codomain[ codomain[x] - 1 ]:
            print("NO")
            exit()
        
    print("YES")

else:
    print("NO")