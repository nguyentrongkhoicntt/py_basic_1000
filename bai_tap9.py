# Bài 9: Tính T(n) = 1 x 2 x 3…x N
s = 1
n = 6
for x in range(1, n):
    s = s * x
    print("x = " + str(x) + " => " + "x = " + str(s))
    print("s = " + str(s))

print("sum of 1 x 2 x 3 x … x " + str(n) + " = " + str(s))