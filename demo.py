
# husband_name = input("Enter your name: ")
# wife_name = input("Enter your wife name: ")
# husband_age = int(input("Enter your age: "))
# wife_age = int(input("Enter your wife age: "))

# if husband_age >= 19 and wife_age >= 15:
#     print("You are a lovely/romantic couple.")
# elif husband_age >= 19 and wife_age >= 20:
#     print("You are a very cute/lovely/romantic couple.")
# else:
#     print("You are a cute old couple.")


# for i in range(1, 101, 1):
#     print(i, end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississippi")

# print("Thank You")

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num)
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
# num.reverse()
# print(num)

# l = [11, 45, 1, 2, 4, 6]
# print(l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
# print(l.index(1))
# print(l.count(2))
"""m = l.copy()
m[0] = 0
print(m)"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

user_input = int(input("Enter Celsius Degrees: "))
converted_celsius = celsius_to_fahrenheit(user_input)
print(converted_celsius)




s5={2,4,6,8,10,12,14,16}

def check_presence(n , s):
    if n in s:
        return f"{n} is here"
    else:
        return f"{n} is absent"

print(check_presence(2, s5))



def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")



def gcd_iterative(a, b):
    while b  != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd_iterative(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")




# def is_prime(number):
#   if number < 2:
#     return False
#   for i in range(2, number):
#     if number % i == 0:
#       return False
#   return True

# user_input = int(input("Enter the number here: "))
# if is_prime(user_input):
#   print(f"{user_input} is prime")
# else:
#   print(f"{user_input} is not prime")


# def is_palindrome(astring):
#   astring = astring.lower()
#   reversed_st = astring[::-1]
#   if astring == reversed_st:
#     return True
#   else:
#     return False

# user_input = input("Enter the number here: ")

# if(is_palindrome(user_input)):
#   print(f"{user_input} is palindrome")
# else:
#   print(f"{user_input} is not palindrome")








































































