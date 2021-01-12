##DATA TYPES AND VARIABLES
#1.  You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

#First make a variable for each movie that has the amount of days they are rented.
the_lil_mermaid = 3
brother_bear = 5
hercules = 1

# Then create a variable that has the movie rental price.
rental_fee = 3

#Now determine the total price by multiplying the rental fee times the amount of days for each movie
total_fee = rental_fee * the_lil_mermaid
total_fee = total_fee + brother_bear * rental_fee
total_fee = total_fee + rental_fee * hercules
total_fee
#Total rental fee is $27

#2.  Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

#First make variables for pay rate for each company

google = 400
amazon = 380
facebook = 350

#make variables for hours worked for each company

google_hours = 6
amazon_hours = 4
facebook_hours = 10

#Find total pay by multiplying the pay rate times the hours

google_pay = google * google_hours
amazon_pay = amazon * amazon_hours
facebook_pay = facebook * facebook_hours

#Sum pay from each company for total payment 

total = google_pay + amazon_pay + facebook_pay
#total pay = $7420

#3.  