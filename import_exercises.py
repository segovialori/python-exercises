##IMPORT EXERCISES
#example 1
import math
math.sqrt(4)
import math
from math import sqrt

print(sqrt(16))
print(math.pow(4,2))

#example 2
import pandas as pd

pd.read_clipboard()

from pandas import read_clipboard 

read_clipboard
#Import and test 3 of the functions from your functions exercise file.
#Import each function in a different way:
#- import the module and refer to the function with the . syntax
#- use from to import the function directly
#- use from and give the function a different name
import function_exercises
from functions_lesson import increment

#ITERTOOLS

#1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools as it
len(list(it.product([1, 2, 3], 'abc')))
#9

#2. How many different ways can you combine two of the letters from "abcd"?
len(list(it.combinations('abcd', 2)))
#6

#Total number of users
import json
profiles = json.load(open('profiles.json'))
#19

profiles[0]
profiles[0]
len(profiles)
profiles[18]

#2.  Number of active users
#print(my_dict.get('age'))
#profiles is a list so I can't use .get on a list
#Example:  for forecast in Blacksburg_Forecast: 
     #wind_speed = forecast['wind']  
     #print(wind_speed)
#19 total, 10 false, 9 True
for active_user in profiles:
    is_active = active_user['isActive']
    active_count = []
    if is_active == True:
        print(is_active)
#3.  Number of inactive users
# Need to count the boolean values by converting them
for active_user in profiles:
    is_active = active_user['isActive']
    active_count = []
    if is_active == False:
        print(is_active)
#function for user name and user active status
for name_and_status in profiles:
    name_active = name_and_status['name'],name_and_status['isActive']
    print(name_active)
#4.  Grand total of balances for all users
#need to remove commas from balance values and change str to float so I can sum
#replace:  string.replace(oldvalue, newvalue, count)
for balance_user in profiles:
    balance_per_user = balance_user['balance']
    balance_per_user = balance_per_user.replace('$', '')
    balance_per_user = balance_per_user.replace(',','')
    balance_per_user = float(balance_per_user)
    
    print(balance_per_user)        
#5.  Average balance per user
#6.  User with the lowest balance
#7.  User with the highest balance
#8.  Most common favorite fruit
for fav_fruit in profiles:
    user_fruit = fav_fruit['favoriteFruit']
    print(user_fruit)

#9. Least most common favorite fruit
#10.   Total number of unread messages for all users
for entire_message in profiles:
    user_message = entire_message['greeting']
    print(user_message)
    