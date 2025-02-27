print("*****tution center*******")
students_names=["sachien","daniel","vijay","manikandan","james"]
print(students_names)
name=input("enter the name :")
if name in students_names:
    print("your are student of this tution ")
else:
    print("you are not a student of this tution")
print("\n")

print("********silunu oru kadhal*****")
ishwarya=input("whether he left or not:")
if(ishwarya=="left"):
    print("Gowtham marry kundhavi")
else:
    print("gowtham marry ishwarya") 
print("\n")

print("************century year*********")
year = int(input("Enter a year: "))
if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")
print("\n")

balance_amount = 1000
withdraw_amount = float(input("Enter withdrawal amount: "))
if withdraw_amount > balance_amount:
    print("Insufficient funds.")
else:
    balance_amount -= withdraw_amount
    print(f"Withdrawal successful. Remaining balance: ${balance_amount}")
print("\n")    

print("********VOWELS OR CONSONANT********")
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
print("\n")    
        
print("*******alphabet or numeric********")
char = input("Enter a character: ")
if char.isalpha():
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")
print("\n")

print("************Uppercase or not**********")
text = input("Enter a string: ")
if text.isupper():
    print(f"{text} is in uppercase.")
else:
    print(f"{text} is not in uppercase.")
print("\n")

print("************float or integer**********")
num = input("Enter a number: ")
if '.' in num:
    print(f"{num} is a float.")
else:
    print(f"{num} is an integer.")
print("\n")    

income = float(input("Enter your monthly income: "))
if income >= 5000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")

      
print("*********bike insurance********")
age = int(input("Enter your age: "))
if age >= 18 and age <= 70:
    print("You are eligible for car insurance.")
else:
    print("You are not eligible for car insurance.")





