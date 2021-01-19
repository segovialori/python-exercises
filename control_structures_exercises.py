#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##CONTROL STRUCTURES EXERCISES

#1.  CONDITIONAL BASICS
#1A.  prompt the user for a day of the week, print out whether the day is Monday or not

#how to i apply string methods directly to input?
-Justin suggested:  Input(lower())- tried this and it doesnt work 
-Tried .lower() after input and it changed user input to all lowercase
####

day_of_the_week = input('What day of the week is it? ').lower()

if day_of_the_week == 'monday':
    print('Mondays amirite')
else:
    print(f'{day_of_the_week} is better than Monday')
#1B.  prompt the user for a day of the week, print out whether the day is a weekday or a weekend
what_day_is_it = input('What day is it? ')

if what_day_is_it == "saturday":
    print('weekend')
elif what_day_is_it == "sunday":
    print('weekend')
else:
    print('weekday')

##Zach way
if weekday_selection == "saturday" or weekday_selection == "sunday"
#or
if weekday_selection.lower().startswith('s'):


# In[11]:


#1C.  create variables and make up values for
# the number of hours worked in one week
hours_worked = float(input('how many hours did you work? '))

# the hourly rate
hourly_rate = float(input('what is your hourly rate? '))

# how much the week's paycheck will be
pay_check = (hours_worked * hourly_rate)

# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

if hours_worked <= 40:
    print('Expect a pay check for $',pay_check)
else:
    hours_worked > 40
    print('Expect a pay check with overtime included for $',(hours_worked - 40) * (hourly_rate * 1.5) + (40 * hourly_rate))


# # 2.  Loop Basics
# 
# ## a.  While
# 
# ### - Create an integer variable i with a value of 5.
# ### - Create a while loop that runs so long as i is less than or equal to 15
# ### - Each loop iteration, output the current value of i, then increment i by one.

# In[3]:


i = 5
while i <= 15:
    print(i)
    i += 1


# ### Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# ### Alter your loop to count backwards by 5's from 100 to -10.
# ### Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# #### 2
# #### 4
# #### 16
# #### 256
# #### 65536

# In[12]:


number = 0
while number <= 50:
    print(number * 2)
    number += 1
  


# In[15]:


#zach way

i = 0
while i <= 100:
    print(f"i:{i}")
    i += 2


# In[22]:


i = 100
while i >= -10:
    print(f"i:{i}")
    i -= 5


# In[20]:


i = 2
while i <= 1_000_000:
    print(f"i:{i}")
    i *= i


# In[24]:


i = 100
while i >= 5:
    print(i)
    i -= 5


# In[25]:


x = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{x} x {i} = {x * i}")


# In[26]:


for i in range(1,10):
    print(str(i) * i)


# In[28]:


user_num = int(input("Enter odd number between 1 and 50: "))

i = 1
while i <= 50:
    if i == user_num:
        print(f"skip: {i}")
        i += 2
        continue
    print(f"Here is an odd number: {i}")
    i += 2


# In[31]:


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# In[34]:


user_input = int(input("Enter an integer: "))
print()
print("number | squared | cubed")
print("------ | ------- | -----")
for i in range(1, user_input + 1):
    print(f"{i} | {i**2} | {i**3}")
    
#format loop
print("%6d | %7d | %5d" % {i}, {i**2}, {i**3})


# In[36]:


numeric_grade = 88

if numeric_grade >= 88:
    print('A')
elif numeric_grade >= 80:
    print('B')
elif numeric_grade >= 67:
    print('C')
elif numeric_grade >= 60:
    print('D')
else:
    print('F')


# In[41]:


books = [
    {"Title": "The Man Who Mistook His Wife for a Hat", "Author": "Oliver Sacks", "Genre": "Non-fiction"},
    {"Title": "The Bell Jar", "Author": "Slyvia Plath", "Genre": "Non-fiction"},
    {"Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Genre": "Non-fiction"}
]
   
selected_genre:  input("pick a genre: ")
selected_books = [book for book in books if book ['genre'] == selected_genre]
for book in books:
     print("---")
     print("Title: {}".format(book['Title'])
     print("Author: {}".format(book['Author'])
     print("Genre: {}".format(book['Genre'])


# In[ ]:




