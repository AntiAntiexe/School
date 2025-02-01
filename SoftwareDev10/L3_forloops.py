import pandas as pd

df = pd.read_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv')
user = input('User: ')
password = int(input('Pass: '))

data = df[df['username']== user]

if user in df['username'].tolist() and password in data['password'].to_list():
    print(f'hello {user}.')
else:
    print('Incorrect username or password.')


print(df[df['username']== user])