



number  =int(input("Enter a 5 digit number: "))

first= (number//10000)
second =((number//1000)%10)
third = ((number%1000)//100)
fourth= ((number//100)%10)
fifth = (number%10)


print(first, second, third, fourth, fifth)
