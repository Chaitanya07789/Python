# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# using lambda function
is_leap_year = lambda year: True if (year%4==0 and year%100!=0) or (year%400==0) else False

year =2020
print(f"{year} is a leap year : {is_leap_year(year)}")
