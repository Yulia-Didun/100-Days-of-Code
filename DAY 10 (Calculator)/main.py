import os
from art import logo

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {
  '+': add, 
  '-': subtract, 
  '*': multiply, 
  '/': divide,
}


def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for operation in operations:
    print(operation)
    
  should_continue = True
  
  while should_continue:
    chosen_operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
  
    calculation_function = operations[chosen_operation]
    result = calculation_function(num1, num2)
    print(f"\n{num1} {chosen_operation} {num2} = {result}")

    next_calculation = input(f"\nType 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'x' to exit: ")
    
    if next_calculation == 'y':
      num1 = result
    elif next_calculation == 'n':
      should_continue = False
      os.system("cls")
      calculator()
    else:
      should_continue = False
  
calculator()