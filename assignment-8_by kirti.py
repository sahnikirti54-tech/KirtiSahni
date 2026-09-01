#assignment 8
'''
#1. add_number(a,b)
def add_numbers(a,b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an int or float")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an int or float")
    return a + b

print(add_numbers(10, 20))
'''
#rectangle_area
'''
def rectangle_area(length, width):
    if not isinstance(length, (int, float))or isinstance(length, bool):
        raise TypeError("length must be numeric")
    if not isinstance(width, (int, float)) or isinstance(width, bool):
        raise TyprError("width must be numeric")
    if length <=0 or width <=0:
        raise ValueError("length and width must be greater than 0")
    return length * width

print(rectangle_area(10, 5))

'''
#3. student_full_name()
'''
def student_full_name(first_name, last_name):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("Names must be strings")
    return f"{first_name.title()} {last_name.title()}"
print(student_full_name("krishna", "gandhi"))
print(student_full_name(first_name="krishna", last_name="gandhi"))
'''
#4. calculate_simple_interest()
'''
def calculate_simple_interest(principal, rate, time):
    values = (principal, rate, time)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool)for x in values):
        raise TypeError("All parameters must be numeric")
    if any(x < 0 for x in values):
        raise ValueError("Parameters cannot be negative")
    return (principal * rate * time) / 100

print(calculate_simple_interest(10000, 5, 2)) 

'''
#5 power()
'''
def power(base, exponent=2):
    if not isinstance(base, (int, float)) or isinstance(base, bool):
        raise TypeError("base must be numeric")
    if not isinstance(exponent, (int, float)) or isinstance(exponent, bool):
        raise TypeError("exponent must be numeric")
    return base ** exponent
print(power(5))       
print(power(2, 3)) 
'''
#6 greet_student()
'''
def greet_student(name, message="Welcome to Python Programming"):
    if not isinstance(name, str) or not isinstance(message, str):
        raise TypeError("name and message must be strings")
    if not name.strip() or not message.strip():
        raise ValueError("name and message cannot be empty")
    return f"Hello {name}, {message}"
print(greet_student("Krishna"))
print(greet_student("Krishna", message="Good morning!")) 

'''
#7. convert_temperature()
'''
def convert_temperature(celsius, scale="F"):
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError("celsius must be numeric")
    if not isinstance(scale, str):
        raise TypeError("scale must be a string")
    scale = scale.upper()
    if scale not in ("F", "K"):
        raise ValueError("scale must be 'F' or 'K'")
    if scale == "F":
        return (celsius * 9 / 5) + 32
    return celsius + 273.15

print(convert_temperature(25))
print(convert_temperature(25, "K")) 
'''
#8. calculate_bill()
'''
def calculate_bill(amount, tax_rate=5):
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise TypeError("amount must be numeric")
    if not isinstance(tax_rate, (int, float)) or isinstance(tax_rate, bool):
        raise TypeError("tax_rate must be numeric")
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if not 0 <= tax_rate <= 100:
        raise ValueError("tax_rate must be between 0 and 100")
    tax = amount * tax_rate / 100
    return amount + tax
print(calculate_bill(1000))
print(calculate_bill(1000, tax_rate=18))
'''
#9.find_maximum()
'''
def find_maximum(a, b, c):
    values = (a, b, c)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) for x in values):
        raise TypeError("All arguments must be numeric")
    return max(values)

print(find_maximum(10, 25, 15))
'''
#10 is_eligible_for_vote()
'''
def is_eligible_for_vote(age, citizenship=True):
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("age must be an integer")
    if not isinstance(citizenship, bool):
        raise TypeError("citizenship must be Boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18 and citizenship

print(is_eligible_for_vote(20))
print(is_eligible_for_vote(17, citizenship=True)) 
'''
#11. calculate_discount()
'''
def calculate_discount(price, discount_percent=10):
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise TypeError("price must be numeric")
    if not isinstance(discount_percent, (int, float)) or isinstance(discount_percent, bool):
        raise TypeError("discount_percent must be numeric")
    if price <= 0:
        raise ValueError("price must be greater than 0")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    return price - (price * discount_percent / 100)

print(calculate_discount(1000))
print(calculate_discount(1000, discount_percent=20))
'''
#12.salary_after_bonus()
def salary_after_bonus(salary, bonus_percent=5):
    if not isinstance(salary, (int, float)) or isinstance(salary, bool):
        raise TypeError("salary must be numeric")
    if not isinstance(bonus_percent, (int, float)) or isinstance(bonus_percent, bool):
        raise TypeError("bonus_percent must be numeric")
    if salary < 0 or bonus_percent < 0:
        raise ValueError("salary and bonus_percent cannot be negative")
    return salary + (salary * bonus_percent / 100)

print(salary_after_bonus(50000))
print(salary_after_bonus(50000, bonus_percent=10)) 


















