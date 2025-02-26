import pandas as pd
import re

df = pd.read_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv')
'''user = input('User: ')
password = int(input('Pass: '))

data = df[df['username']== user]

if user in df['username'].tolist() and password in data['password'].to_list():
    print(f'hello {user}.')
else:
    print('Incorrect username or password.')


print(df[df['username']== user])'''

txt = "dib0003@gwsc.vic.edu.au@"
x = re.findall("@gwsc.vic.edu.au", txt)
print(x) 


txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) 