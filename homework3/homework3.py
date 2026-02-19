# File Name: homework 3 (Functions and Conditionals)
# Note: I tested all my functions with values 
# --- Print Functions ---
def say_goodbye(name):
    print("Goodbye,", name)
# say_goodbye("Hannah")

def circle_area(radius):
    # calculates circle area
    print(radius ** 2 * 3.14)
# circle_area(5)

# --- Return Functions ---
def subtract(a, b):
    return a - b
# print(subtract(10, 3))

def multiply(c, d):
    return c * d
# print(multiply(20, 5))

def divide(e, f):
    return e / f
# print(divide(40, 8))

# --- Conditionals ---
temperatures = [39, 44, 66, 52, 40, 59]
def what_to_wear(temperatures):
    return (min(temperatures), max(temperatures))
# print(what_to_wear(temperatures))

def is_weekend(num):
 if num == 6 or num == 7:
  return "True"
 else:
  return "False"
 
# print(is_weekend (7)) # 7 represents Sunday, should output true

def fuel_efficiency(distance, fuel):
   return distance / fuel
# print(fuel_efficiency(250, 12))

def secret_code(num):
   # couldn't figure out for the longest time how to not already assume the length of digits so hopefully this is correct-adjacent?
   core =  num // 10 
   remainder = num % 10
   number_of_digits = len(str(core))
   return remainder * (10 ** number_of_digits) + core
num = 987654
result = secret_code(num) # 987654 should be (floor) divided by 10, the remainder should be multiplied by the number of digits, and these two numbers should be added
print(f"The result of my secret code function (5.4) with num = {num} is {result}.")

# --- Loops ---
def oski_stole_power(x, y):
  result_value = 1
  for i in range(y):
     result_value *=  x
  return result_value

# print(oski_stole_power(2,7))

int_list = [4, 9, 15, 20, 33, 21, 2, 42, 6]
def oski_stole_min_for(int_list):
   min_value = int_list[0]
   for number in int_list:
      if number < min_value:
         min_value = number
   return min_value
# print("Minimum Value of List:", oski_stole_min_for(int_list))

def oski_stole_max_for(int_list):
   max_value = int_list[0]
   for number in int_list:
      if number > max_value:
         max_value = number
   return max_value 
# print("Maximum Value of List:", oski_stole_max_for(int_list))

def oski_stole_min_while(int_list):
   min_val = int_list[0]
   for number in int_list:
      if number < min_val:
         min_val = number
   return min_val
# print("Minimum Value of List:", oski_stole_min_while(int_list))

def oski_stole_max_while(int_list):
   max_val = int_list[0]
   for number in int_list:
      if number > max_val:
         max_val = number
   return max_val
# print("Maximum Value of List:", oski_stole_max_while(int_list))
    
def add_digits(num):
   total = 0
   for digit in str(num):
       total += int(digit)
   return total

# print(add_digits(2468))