
def LCSLength(X, Y):
    m = len(X)
    n = len(Y)

    # let b[1... m, 1... n] and c[0... m, 0... n] be new tables, we are making a matrix array
    c = [[0] * (n+1) for _ in range(m+1)] # LCS lengths
    b = [[""] * (n+1) for _ in range(m+1)] # directions

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] +1
                b[i][j] = "northwest"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "north"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "west"

    return c, b

def printLCS(b, X, i, j):
    if i==0 or j==0:
        return ""
    if b[i][j] == "northwest":
        return printLCS(b, X, i-1, j-1) + X[i-1]
    elif b[i][j] == "north":
        return printLCS(b, X, i-1, j)
    else:
        return printLCS(b, X, i, j-1)
    
# input
X = input("Enter the first sequence: ")
Y = input("Enter the second sequence: ")
c, b = LCSLength(X, Y)
result = printLCS(b, X, len(X), len(Y))

# Output
print("Length of LCS:", c[len(X)][len(Y)])
print("LCS:", result)