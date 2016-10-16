def sieve(n):
    composites = set()
    result = []
    for i in range(2, n):
        if i not in composites:
            result.append(i)
            composites.update(range(i * i, n, i))
    return result


N = int(input())
primes = sieve(N)
result = list(set([i * j for i in primes for j in primes if i * j <= N]))
result.sort()
for i in result:
    print(i,end=' ')
