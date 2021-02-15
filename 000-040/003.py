n = 600851475143

result = []

for i in range(2,n):
    if n%i == 0:
        result.append(i)
        print(i)
        n /=i

print(result)