

negative=0
positive=0
zero=0
numbercounter=0

while(numbercounter<5):
 number=int(input('Enter a number'))
 if(number<0):
  negative+=1 
 elif(number>0):
  positive+=1
 else:
  zero+=1
 numbercounter+=1

print('There are ', negative, ' negative numbers')
print('There are ', positive, ' negative numbers')
print('There are ', zero, ' zero numbers')

