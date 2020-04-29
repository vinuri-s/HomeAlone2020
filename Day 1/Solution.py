
# Code from GeeksforGeeks
# Tutorial Link - https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

def find_max_sum(arr): 
    incl = 0
    excl = 0
     
    for i in arr: 
          
        # Current max excluding i (No ternary in  
        # Python) 
        new_excl = excl if excl>incl else incl 
         
        # Current max including i 
        incl = excl + i 
        excl = new_excl 
      
    # return max of incl and excl 
    return (excl if excl>incl else incl) 


arr = list(map(int,input().strip().split()))
print(find_max_sum(arr))
