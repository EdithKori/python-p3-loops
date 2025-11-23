#!/usr/bin/env python3

def happy_new_year():
    num = 10  # start at 10
    while num >= 1:
        print(num)
        num -= 1 
    print("Happy New Year!")

   

def square_integers(int_list):
    squared_list = []
    for int in int_list:
        squared_list.append(int ** 2)
    return squared_list
    
    
    
def fizzbuzz():
    for num in range(1, 101):  # numbers from 1 to 100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)