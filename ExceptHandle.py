#Exception Handling example

num1 = int(input ("Enter first Number :"))
num2 = int(input ("Enter second Number :"))

try:
 print("Division of %d %d = %d " %(num1,num2,num1/num2))
except ZeroDivisionError:
 raise ValueError("divisor must not be zero") from None
#except Exception as other:
#    print("Something else broke: ",other)