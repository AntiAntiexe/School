from datetime import datetime

dob = input('Date of Birth (day/month/year): ')
current_year = datetime.now().year
age = int(dob[6:10]) - current_year

print(f'You are currently {age} years old!')





