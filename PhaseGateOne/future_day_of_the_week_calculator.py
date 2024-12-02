"""
Create a list that holds the 7 days of the week name it days of the week
prompt user to enter todays day
save it as todays day
prompt user to enter number of days since today
future index = (futuredaynumber + todaysday) % 7
the index of futureindex in the list created in stage 1 is the future day
print it
"""


days_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

todays_day = int(input("Enter today's day:"))

future_day_number = int(input("Enter the number of days since today:"))

future_day_index = (future_day_number + todays_day) % 7

calculated_day_of_the_week = days_of_the_week[future_day_index]

print("Today is",days_of_the_week[todays_day] ,"and the future day is", calculated_day_of_the_week )