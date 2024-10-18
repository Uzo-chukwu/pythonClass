number  =int(input("Enter a number between 100 - 999: "))

first= (number//100)
second =((number//10)%10)
last = (number%10)

print(last, second, first)


if first%2 ==0:
 print(first, 'is an even number') 
if first%2 !=0:
 print(first, 'is an odd number') 
if second%2 ==0:
 print(second, 'is an even number') 
if second%2 !=0:
 print(second, 'is an odd number') 
if last%2 ==0:
 print(last, 'is an even number') 
if last%2 !=0:
 print(last, 'is an odd number') 

