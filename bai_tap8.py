# Bài 8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2
s = 0
n = 6
for x in range(1, n):
    s = s + (2*x + 1)/(2*x + 2)
    print("x = " + str(x) + " => " + "(2*x + 1)/(2*x + 2)  =" + str(s))
    print("s = " + str(s))

print("sum of ½ + ¾ + 5/6 + … + " + str(n+1) + "/" + str(n+2) + "=" + " " + str(s))