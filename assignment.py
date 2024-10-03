#No. 1)
# The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")

#No. 2)
# Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 

# Function to calculate the area of a triangle
def triangle_area(base, height):
    area = 0.5 * base * height
    return area
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")

#No 3)
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 

# Function to determine the grade based on the score
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 50 <= score <= 59:
        return 'E'
    elif score < 50:
        return 'Fail'
    else:
        return 'Invalid score'

# Input the score from the user
score = float(input("Enter the student's score (0-100): "))

# Determine the grade
grade = determine_grade(score)

# Display the grade
print(f"The student's grade is: {grade}")

#No 4)
#WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.
# Class to represent the WITIAcademy Sacco system
class WITIAcademySacco:
    def __init__(self):
        self.balance = 0
    
    # Function to deposit money
    def deposit(self, amount):
        if amount >= 1000:
            self.balance += amount
            print(f"Successfully deposited {amount}. Your new balance is {self.balance}.")
        else:
            print("Minimum deposit amount is 1000.")

    # Function to withdraw money
    def withdraw(self, amount):
        if amount >= 500:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Successfully withdrew {amount}. Your new balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Minimum withdrawal amount is 500.")

    # Function to check balance
    def check_balance(self):
        print(f"Your current balance is {self.balance}.")

# Function to run the Sacco platform
def sacco_platform():
    sacco = WITIAcademySacco()
    
    print("Welcome to WITIAcademy Sacco!")
    
    while True:
        print("\nPlease select an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            sacco.deposit(amount)
        
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            sacco.withdraw(amount)
        
        elif choice == '3':
            sacco.check_balance()
        
        elif choice == '4':
            print("Thank you for using WITIAcademy Sacco. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the Sacco platform
sacco_platform()


