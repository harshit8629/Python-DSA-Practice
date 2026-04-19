dividend = 10
divisor = 3

if dividend == -2147483648 and divisor == -1:
    print(2147483647)
if(dividend ==0):
    print(0)
elif(divisor ==0):
    print("Invalid")
    counter=0
if dividend>0 and divisor >0:
    print(dividend//divisor)
elif dividend<0 and divisor<0:
    print(dividend//divisor)
elif dividend<0 and divisor>0:
    counter = -1
    print(counter*(abs(dividend)//abs(divisor)))
elif dividend >0 and divisor <0:
    counter = -1
    print(counter*(abs(dividend)//abs(divisor)))

