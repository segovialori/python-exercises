#!/usr/bin/env python
# coding: utf-8

# # Python Functions
# 
# - Context: what are functions? why are they helpful?
# 

# - functions are resusable pieces of code
# - accepts inputs and produce outputs
# - abstraction
# - when we execute a function, we call that a function "call" (invoking the function)
# 
# 

# ## Using Functions

# <div style="padding: 1em 3em; border: 1px solid black;">
#     <div style="font-weight: bold; font-size: 1.2em; border-bottom: 1px dashed black; padding-bottom: .5em;">
#         Vocab
#     </div>
#     <ul>
#         <li>Run/invoke/call</li>
#         <li>Argument</li>
#         <li>Return Value</li>
#     </ul>
# </div>

# - when we invoke a function we are calling arguments that are being passed to the function
# - function calls bring a return value
# - 

# We've already used built-in functions

# <div style="background-color: rgba(0, 100, 200, .1); padding: 1em 3em; border-radius: 5px; border: 1px solid black">
#     <div style="font-weight: bold; font-size: 1.2em; border-bottom: 1px dashed black; padding-bottom: .5em;">
#         Mini Exercise -- Using Functions
#     </div>
#     <ol>
#         <li>
#             <p>Take a look at this code snippet:</p>
#             <pre><code>max([1, 2, 3])</code></pre>
#             <p>What is the function name?</p>
#             <p>Where is the function invocation?</p>
#             <p>What is the return value?</p>
#         </li>
#         <li>
#             <p>Take a look at this code snippet:</p>
#             <pre><code>type(max([1, 2, 3]))</code></pre>
#             <p>What will the output be? Why?</p>
#         </li>
#         <li>
#             <p>Take a look at this code snippet:</p>
#             <pre><code>type(max)</code></pre>
#             <p>What will the output be? Why?</p>
#         </li>
#         <li>
#             <p>What is the difference between the two code blocks below?</p>
#             <pre><code>print</code></pre>
#             <pre><code>print()</code></pre>
#         </li>
#         <li>What other built in functions do you know?</li>
#     </ol>
# </div>

# In[1]:


max([1,2,3])


# - the function name is max
# - the function invocation is where the open parentheses are :name, parenthesis, and anything inside it
# - the return value is 3

# In[2]:


type(max([1, 2, 3]))


# - The output will be the type of what is returned in the max function because it is just asking for the type.

# In[3]:


type(max)


# -the output will be function bc max is a function

# #### What is the difference between the two code blocks below?
# - print
# - print()
# - The differnce is that one is a function and the other is not.  One is calling the function and the other is not.  

# #### What other built in functions do you know?
# - min(), avg(), sum(), def()

# ## Function Signature
# - the type and quantity of the function arguments plus the function's return type.
# - what does it take and and what does it produce out
# - e.g:  max(l: list[int]) -> int

# In[ ]:


#### What are the signatures of the print function and the range function


# - print():  takes in a string, int, float
# - print(x):   its return value is none
# - range(start: int, stop: int[, step: int]): takes in start: int, stop: int -> list[int]
# - range:  takes in two arguments, both integers, and returns list (range) of integers.  Also has an optional 3rd agrument
# 

# ## Defining Functions

# <div style="padding: 1em 3em; border: 1px solid black;">
#     <div style="font-weight: bold; font-size: 1.2em; border-bottom: 1px dashed black; padding-bottom: .5em;">
#         Vocab
#     </div>
#     <ul>
#         <li>Function Definition</li>
#         <li>Function Name</li>
#         <li>Argument</li>
#         <li>Parameter</li>
#         <li>Function Body</li>
#     </ul>
# </div>

# In[4]:


def increment(n):
    return n + 1
# 2 is the argument of the invocation of the increment function
increment(2)


# - we can name our functions whatever we want
# - try to name functions as verbs
# - n is the parameter in the function, the place holder/argument of the function

# increment(n:int) -> int

# <div style="background-color: rgba(0, 100, 200, .1); padding: 1em 3em; border-radius: 5px; border: 1px solid black">
#     <div style="font-weight: bold; font-size: 1.2em; border-bottom: 1px dashed black; padding-bottom: .5em;">
#         Mini Exercise -- Defining Functions
#     </div>
#     <ol>
#         <li>What is the difference between calling and defining a function?</li>
#         <li>
#             <p>What is the difference between the two code blocks below?</p>
#             <pre><code>def increment(n):
#     return n + 1</code></pre>
#             <pre><code>def increment(n):
#     print(n + 1)</code></pre>
#         </li>
#         <li>Create a function named <code>nonzero</code>. It should accept a number and return true if the number is anythong other than zero, false otherwise.</li>
#         <li>Use your <code>nonzero</code> function in combination with the built-in <code>input</code> function and an <code>if</code> statement to prompt the user for a number and print a message displaying whether or not the number is zero.</li>
#         <li>Transfer the work you have done into a function named <code>explain_nonzero</code>. Calling this function whould prompt the user and display the message as before.</li>
#     </ol>
# </div>

# In[ ]:


#1.  What is the difference between calling and defining a function?
# when you return a function it defines the function
# the other one calls the function


# #2.  What is the difference between the two code blocks below?
# - the return value is passing the argument, the print value is not
# - producing return value and not producing the return value

# In[14]:


#3.  Create a function named nonzero. 
#It should accept a number and return true if the number is anythong other 
#than zero, false otherwise.
def nonzero(n):
    if n > 0:
        return True
    else:
        return False
nonzero(-2)

## Zach way
def nonzero(x):
    return x != 0
nonzero(22)


# nonzero(x:int)->bool

# In[16]:


#4.  Use your nonzero function in combination with the built-in 
#input function and an if statement to prompt the user for a number 
#and print a message displaying whether or not the number is zero.
def nonzero(user_input = input("Input a number: ")):
    if user_input == 0:
         print("Number is zero")
    elif user_input > 0:
         print("Number is greater than zero")
    else:
         print("Number is less than zero")
#zach way

user_input = int(input("Please enter a number: "))

if nonzero(user_input):
    print("That is not zero")
else:
    print("That is zero!")
    
    


# In[19]:


#5.  Transfer the work you have done into a function named explain_nonzero. 
#Calling this function would prompt the user and display the message as before.

def explain_nonzero():
    if nonzero(user_input):
        print("That is not zero")
    else:
        print("That is zero!")
explain_nonzero()


# - what happens if we omit the return keyword?
# -- the function does not return a value
# -- the function call expression evaluates to None
# - when is this useful?
# -- for side effects.  
# -- square_and_double(x): produces a value
# -- insert_book_into_database(book): has a side effect
# -- fill_nulls_with_zero(column):  produces a value -- a new column with nulls filled in
# 

# ### Default Parameter Values and Keyword Arguments

# In[ ]:


def sayhello(name="Easley"):
    return f"Hello, {name}!"

#because he defined a default value, () without anything in it will use the default value
#the name parameter has a default value of "easley"
#passing an agrument for name is optional


# In[22]:


def sayhello(name="Easley", greeting = "Hello"):
    return f"{greeting}, {name}!"
sayhello("Class", "Good Afternoon")


# - postional arguments: parameter defined by position, or order
# - keyword arguments: parameter defined by keyword

# ## Function Scope
# 
# - defining variables inside/outside of functions
# - defines where a variable can be referenced

# <div style="padding: 1em 3em; border: 1px solid black;">
#     <div style="font-weight: bold; font-size: 1.2em; border-bottom: 1px dashed black; padding-bottom: .5em;">
#         Vocab
#     </div>
#     <ul>
#         <li>Scope</li>
#         <li>Global</li>
#         <li>Local</li>
#     </ul>
# </div>

# In[23]:


# NB. function names and variables are very generic here because the concept is very generic
def f():
    x = 123

f()    
print(x)

#The variable x has local scope since it is defined inside the function
#That definition is local, that variable x just exists inside the function
#If we define x outside of our function, then the variable is globally scoper
#Meaning that it is available globally


# In[24]:


x = 123

def f():
    print(x)

f()    


# In[25]:


x = 123 #global

def f(x):
    return x + 1 #local

print(f(12))


# <div style="background-color: rgba(0, 100, 200, .1); padding: 1em 3em; border-radius: 5px; border: 1px solid black">
#     <div style="font-weight: bold; font-size: 1.2em; border-bottom: 1px dashed black; padding-bottom: .5em;">
#         Mini Exercise -- Function Scope
#     </div>
#     <ol>
#         <li>What is the difference between local and global scope? Which is preferred?</li>
#         <li>Take a look at the cell below this one. Before running it, think about what you would expect to happen. Explain step by step how the python code is executing.</li>
#     </ol>
# </div>

# - local scope is within the function and only exists inside the function and global scope is outside the function and exists outside the function
# - local scope is preferred
# - the function is called changeit and will take in a number and add one to it
# - since it is inside the function it will only exist when the function is called
# - x = 42 is a variable that is being created globally
# - print(x) will print 42
# - changeit(x) will not produce anyhting since a number has not been passed.  x is the parameter.  not changing the global variable x.
# - print x will print 42

# In[26]:


def changeit(x):
    x = x + 1

x = 42
print(x)
changeit(x)
print(x)


# ### Function Scope Example
# 
# ```python
# def fill_nulls(df):
#     return df.fillna(0)
#     
# def drop_outliers(df):
#     outlier_cutoff = 3
#     return df[df.zscore().abs() < 3]
#     
# def prep_dataframe(df):
#     df = fill_nulls(df)
#     df = drop_outliers(df)
#     return 
# ```

# [Data Prep example](https://github.com/CodeupClassroom/darden-nlp-exercises/blob/main/nlp_prepare.py). The specifics here aren't important right now, just pay attention to the overall shape of functions and how local scope is used.

# ## Lambda Functions
# 
# - A function as an expression
# - used for "throw away", or one-off, functions

# In[ ]:


def increment(n):
    return n + 1

# same as

increment = lambda n: n + 1


# **Use case**: sorting (min, max too)
# 
# Python doesn't know how to compare dictionaries, but it does know how to compare strings or numbers

# In[30]:


students = [
    {"name": "Ada Lovelace", "grade": 87},
    {"name": "Thomas Bayes", "grade": 89},
    {"name": "Christine Darden", "grade": 99},
    {"name": "Annie Easley", "grade": 94},
    {"name": "Marie Curie", "grade": 97},
]


# - students is a list that holds dictionaries
# 

# In[27]:


sorted([-4,21,3,50,9])


# In[28]:


sorted(students)


# - python doesnt have a concept of one dictionary being less than another dictionary
# - so if you want to sort students by name, by specifing the key word argument key and its value is going to map one element to a value that can be compared
# - order them low to high by taking each element and looking at the name key and sorting by the value associated in that name key

# In[31]:


# sort by namee
sorted(students, key=lambda s: s["name"])


# In[ ]:


# sort by grade
sorted(students, key=lambda s: s["grade"])


# <div style="background-color: rgba(0, 100, 200, .1); padding: 1em 3em; border-radius: 5px; border: 1px solid black">
#     <div style="font-weight: bold; font-size: 1.2em; border-bottom: 1px dashed black; padding-bottom: .5em;">
#         Mini Exercise -- Lambda Functions &amp; Sorting
#     </div>
#     <p>Write the code necessary to sort the list of student dictionaries by student <em>last</em> name.</p>
#     <p>Hints:</p>
#     <ul>
#         <li>You will need to write a function that takes in a student dictionary and returns just the last name.</li>
#         <li>You can use the <code>.split</code> string method to seperate the first name and the last name.</li>
#     </ul>
# </div>

# In[45]:


students = [
    {"name": "Ada Lovelace", "grade": 87},
    {"name": "Thomas Bayes", "grade": 89},
    {"name": "Christine Darden", "grade": 99},
    {"name": "Annie Easley", "grade": 94},
    {"name": "Marie Curie", "grade": 97},
]


# In[46]:





# In[47]:


#Write the code necessary to sort the list of student dictionaries by student last name.

sorted(students, key=lambda s: s["name"].split(" ")[-1])


# In[ ]:




