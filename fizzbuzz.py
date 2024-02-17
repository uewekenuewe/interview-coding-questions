n = int(input())
    
for i in range(1,n):
    ans = ''
    if i % 3 == 0:
        ans += 'Fizz'
    if i % 5 == 0:
        ans += 'Buzz'
    if ans == '':
        ans = str(i)

    print(ans)
