total=0

print " how mant numbers do you want to add together."
userinput= int(raw_input()) 
for x in range (userinput):
    print "enter number"
    userinput2=int(raw_input())
    total=total + userinput2
print total 

total= []
print 'what numbers do you want in a list'
userinput3 = int(raw_input())

for h in range(userinput3):
    print " enter numbers"
    userinput4= int(raw_input())
    total.append(userinput4)
print sum(total)

factorial = 1


print " what number would you like a factorial of"
num = int(input())
factorial = 1
for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)

def print_factors(x):
  
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter a number: "))

print_factors(num)





