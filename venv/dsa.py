# Program to print the largest common substring
#x is the first substring
#Y is the second substring
#m is the length of X
#n is the length of Y
def lcs(X, Y, m, n):#define lcs function
    L = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    lcs = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs += X[i - 1]
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1

        else:
            j -= 1

    lcs = lcs[::-1]
    print("LCS of " + X + " and " + Y + " is " + lcs)


#X IS COLOUMN AND Y IS ROW
X = input("Enter Column : \n")
Y = input("Enter Row : \n")
m = len(X)
n = len(Y)
lcs(X, Y, m, n)