import sys

sums = 0
average= 0
product = 1
smallest = sys.maxsize
largest= -sys.maxsize -1
for count in range(1,5):
	number = int(input("Enter number: "))
	sums += number
	product *= number 
	if number < smallest:
		smallest = number
	if number > largest:
		largest = number

average = sums/4
print("sum =", sums )
print("average =", average)
print("product =", product )
print("smallest =", smallest )
print("largest =", largest )