num1=0
num2=1

inp=int(input("Enter a range:"))

for i in range(inp):
    print(num1," ")
    num1,num2=num2,num1+num2
