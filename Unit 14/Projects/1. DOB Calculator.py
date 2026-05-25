#! +------------------+
#! |  DOB Calculator  |
#! +------------------+

from datetime import date, datetime

# User birth input
dob_input = input("Enter your DOB (DD-MM-YYYY): ")

# string convert datetime object
dob = datetime.strptime(dob_input, "%d-%m-%Y")

# today's date
today = date.today()

# calc age
age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your age is", age)