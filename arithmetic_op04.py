number = 184
x1, x2, x3 = 0, 0, 0
for num in str(number):
   x3 = number % 10
   x2 = int(number/10)  % 10
   x1 = int(number/100) % 1000

# natija
print("yig'indi =", x1 + x2 + x3)
