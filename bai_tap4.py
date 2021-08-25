#Bài 4: Tính S(n) = ½ + ¼ + … + 1/2n
s = 0
n = 6
for x in range(1, n):
    s = s + 1/(2*x)
    print("x = " + str(x) + " => " + "1/(2*" + str(x) + ") = " + str(1/(2*x)))
    print("s = " + str(s))

print("sum of  1/2 + 1/4+ ... + 1/" + str(2*n) + " ís " + str(s))

