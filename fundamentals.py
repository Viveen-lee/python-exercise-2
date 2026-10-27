# arithmetic
x = 10
x += 3
print (x)
y = 5
y *= 2
print (y)
result = x / y
print (result)

# comparison
a = 5
b = 4
a > b
print (a > b)
b % a
print (b % a) 
c = 9
c <= a
print (c <= a)
final_condition = (a > b) or (b % a) and (c <= a)
print (final_condition)

# conditional statements
score = 75
if score >= 90:
  print("grade is A")
elif score >= 80:
  print("grade is B")
elif score >= 70:
  print("grade is C")
elif score >= 60:
  print("grade is D")
else:
  print("grade is F") 

# combining operators and conditionals
num1 = float(input("enter 1st number: "))
operation = input("enter a operation (+ - * /):")
num2 = float(input("enter 2nd number: "))

if operation == "+":
   result = num1 + num2
   print(round(result, 3))
elif operation == "-":
   result = num1 - num2
   print(round(result, 3))
elif operation == "*":
   result = num1 * num2
   print(round(result, 3))
elif operation == "/":
  if( num2==0 ):
    print(round(0))
  else:
    result = num1 / num2
