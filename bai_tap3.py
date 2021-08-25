#  Tính S(n) = 1 + 2 + 3 + … + n
s = 0
n = 13
for x in range(1, n):
  s = s + x

print("sum of 1 + 2 + ...+ " + str(n) + " is " + str(s))
