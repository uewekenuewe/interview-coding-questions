import math
ans = True  
s = str(input())
n = math.floor(len(s)/2) 
for i in range(n):
    if s[i] != s[len(s)-1-i]:
        ans = False 
        break 

print(s,'is palindrome?',ans)

