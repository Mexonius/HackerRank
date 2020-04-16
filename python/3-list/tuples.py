# https://www.hackerrank.com/challenges/python-tuples/problem?h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) # a tuple, not a list
    totuple = tuple(integer_list)
    print( hash(totuple) )