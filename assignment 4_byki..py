#print number from 10 to 1
'''
for i in range(10, 0 , -1):
    print(i)
'''

#print "hello world" infinity times
'''
while True:
    print("hello world")
'''
#find the sum of digits of number
'''
num = int(input("enter a number: "))
digit_sum = 0

while num > 0:
    digit_sum += num % 10
    num //= 10

print("sum of digit:", digit_sum)   
'''
#check weather a number is a palindrorme
'''
original_num = int(input("enter a number: "))
num = original_num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome. ")
else:
    print(f"{original_num} is not a palindrome. ")
'''
#check armstrong number
'''
num = int(input("enter a number: "))
sum_of_cubes = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //=10
if num == sum_of_cubes:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number

'''
# menu-drive calculator (while loop)
'''
while True:
    print("\n--- MENU ---")
    print("1. ADD")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("enter choice(1 - 5):"))
    if choice == 5:
        print("exiting calculator...")
        break
    if choice in (1, 2, 3, 4):
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number:"))
        if choice == 1:
            print("result:", num1 + num2)
        elif choice == 2:
            print("result:", num1 - num2)
        elif choice == 3:
            print("result:", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print("result:", num1 / num2)
            else:
                print("error! division by zero.")
        else:
            print("invalid choice! please enter between 1 - 5")
        
'''
#8.
'''
correct_password = "python123"

while True:
    user_input = input("enter password: ")
    if user_input == correct_password:
        print("access granted!")
        break
    else:
        print("Incorrect password. Try again.")
'''
#fibonacci series (while loop)
n_terms = int(input("how many terms? "))
a, b = 0, 1
count = 0
print("fibonacci series:")
while count < n_terms:
    print(a, end=" ")
    nth = a + b

    a = b
    b = nth
    count += 1
print()
















          
