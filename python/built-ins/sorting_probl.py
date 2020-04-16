# https://www.hackerrank.com/challenges/ginorts/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    # Sample Input
    # Sorting1234
    # Sample Output
    # ginortS1324

s=sorted(input())
print( "".join(
    [x for x in s if x.islower()] + 
    [x for x in s if x.isupper()] +
    [x for x in s if not x.islower() and not x.isupper() and int(x)%2!=0] +
    [x for x in s if not x.islower() and not x.isupper() and int(x)%2==0]
))