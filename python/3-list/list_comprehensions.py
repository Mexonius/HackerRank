# https://www.hackerrank.com/challenges/list-comprehensions/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # SENZA List Comprehension
    # l = list()
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for z in range(z+1):
    #             if i+j+z != n:
    #                 l.append( list( (i,j,z) ) )
    # print(l)

    # Con la List Comprehension, cioè la soluzione corretta
    res = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n ]    
    print(res)