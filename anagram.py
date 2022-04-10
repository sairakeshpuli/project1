n = int( input())
for i in range(n):
    a,b = input().split()
    if sorted(a) == sorted(b):
        
        print("YES",end = " ")
    else:
        print("NO",end=" ")