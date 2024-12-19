
def cutRod(p, n):
    if n==0:
        return 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i-1] + cutRod(p, n-i))
        return q


# input
rod_length = int(input("Enter rod length: "))
prices = list(map(int, input("Prices for each length (separated by spaces): ").split()))

# Output the max revenue
print("Max revenue:", cutRod(prices, rod_length))