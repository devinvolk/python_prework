#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function

def hello_user(user_name):
    #Prints 'Hello_USERNAME' when USERNAME is inputted
    print('Hello_' + user_name)
hello_user('USERNAME')

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odd():
    #Prints odd numbers from 1-100
    for number in range(100):
        if number % 2 == 1:
            print(number)

#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    #Returns the largest number in a list
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
#but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(year):
    #Returns True/False if year is a leap year
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.

def is_consecutive(a_list):
    #Returns True/False if all numbers in a list are in consecutive order
    count = 0
    for x in range(len(a_list)-1):
        if a_list[x] == a_list[x+1]-1:
            count += 0
        else:
            count +=1
    if count > 0:
        return False
    else:
        return True