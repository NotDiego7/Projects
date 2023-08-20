# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇 
age_limit = 90

days_per_year = 365
age_limit_in_days = days_per_year * age_limit
total_days_left = age_limit_in_days - (int(age) * days_per_year)

weeks = 52

weeks_per_year = 52
age_limit_in_weeks = weeks_per_year * age_limit
total_weeks_left = age_limit_in_weeks - (int(age) * weeks_per_year)

months = 12

months_per_year = 12
age_limit_in_months = months_per_year * age_limit
total_months_left = age_limit_in_months - (int(age) * months_per_year)

print(f"You have {total_days_left} days, {total_weeks_left} weeks, and {total_months_left} months left.")

#Code above should be depricated since it takes the long-road to calculating the data.