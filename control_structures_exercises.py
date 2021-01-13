##CONTROL STRUCTURES EXERCISES

#1.  CONDITIONAL BASICS
#1A.  prompt the user for a day of the week, print out whether the day is Monday or not

#how to i apply string methods directly to input?
Input(lower())
print ("String with lower() = ", str_input.lower())
####

day_of_the_week = input('What day of the week is it? ')

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
#1C.  create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

