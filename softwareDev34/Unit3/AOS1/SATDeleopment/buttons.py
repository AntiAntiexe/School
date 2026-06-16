a = ['What is the capital of Spain?', 'What is 5 + 7?', 'What is the smallest mammal?', 'What is the chemical symbol for gold?', 'What is the speed of sound?']
b = ['Madrid', '12', 'Bumblebee Bat', 'Au', '343 m/s']

print(list(zip(a, b)))
c = [[question, answer] for question, answer in zip(a, b)]
print(c)
    