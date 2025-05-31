age = input("What is your current age?: ")
age_int = int(age)

days = 365
weeks = 52
months = 12
potential_years = 90

days_for_90years = potential_years * days
weeks_for_90years = potential_years * weeks
months_for_90years = potential_years * months

user_age_day = age_int * days
user_age_week = age_int * weeks
user_age_month = age_int * months

user_day_until_90 = days_for_90years - user_age_day
user_week_until_90 = weeks_for_90years - user_age_week
user_month_until_90 = months_for_90years - user_age_month

print(f"You have {user_day_until_90} days, {user_week_until_90} weeks, and {user_month_until_90} months left")