# Bài 6: Tính S(n) = 1/1×2 + 1/2×3 +…+ 1/n x (n + 1)
s = 0
n = 6
for x in range(1, n):

    s = s + 1/x*(x+1)

    print("x = " + str(x) + " => " + "1/x*(x+1) =" + str(1/x*(x+1)))
    print("s = " + str(s))

print("sum of 1/1×2 + 1/2×3 +…+ 1/" + str(n) + "*" + str(n+1) + " = " + " " + str(s))
