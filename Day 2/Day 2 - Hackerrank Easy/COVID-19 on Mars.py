# Written by: Amesh M Jayaweera
# amesh.17@itfac.mrt.ac.lk


n = int(input())

# f(n) = 2*f(n-1) + 3*f(n-2) this is a recurrence relation
# It can be convert into single formula which is f(n) = (3^n - (-1)^n)/4
ans = (int(pow(3,n)) - int(pow(-1,n)))//4 

print(ans)
