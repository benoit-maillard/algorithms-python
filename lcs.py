def lcs(s1, s2, l1, l2):
    r = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
    s = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]

    
    for i in range(0, l1):
        for j in range(0, l2):
            if (s1[i] == s2[j]):
                r[i+1][j+1] = 1 + r[i][j]
                s[i+1][j+1] = 0
            else:
                if (r[i+1][j] > r[i][j+1]):
                    r[i+1][j+1] = r[i+1][j]
                    s[i+1][j+1] = 1 

                else:
                    r[i+1][j+1] = r[i][j+1]
                    s[i+1][j+1] = 2

    # reconstruct the solution
    i = l1
    j = l2
    lcs = ""

    while (i != 0 and j != 0):
        if s[i][j] == 0:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        elif s[i][j] == 1:
            j -= 1
        else:
            i -= 1
            
    return lcs

s1 = "BABDBA"
s2 = "DACBCBA"

res = lcs(s1, s2, len(s1), len(s2))
print(res)