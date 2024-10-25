

x = int(input("Enter the start of the range: "))
y = int(input("Enter the end of the range: "))
p = int(input("Enter the divisor: "))

count = 0

for i in range(x, y+1):
	if i % p == 0:
		count += 1

print(f"Number of integers divisible by {p} in the range [{x}, {y}]: {count}")