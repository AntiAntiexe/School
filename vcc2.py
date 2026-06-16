from collections import Counter

currentPos = [10, 10]
seed_area = []
lines =[]
with open('sed.txt', 'r') as f:
    for line in f:
        s = line.strip()
        s = s.split(
        )
        if s:
            command = s[0]

            if command == 'N':
                currentPos[1] += 1
            elif command == 'S':
                currentPos[1] -= 1
            elif command == 'E':
                currentPos[0] += 1
            elif command == 'W':
                currentPos[0] -= 1
        if s[1] =="Seed":
            seed_area.append([currentPos[0], currentPos[1]])



if seed_area:
    cnt = Counter(map(tuple, seed_area))
    most_tuple, freq = cnt.most_common(1)[0]
    print(list(most_tuple))  # most recurring coordinate as list
else:
    print(None)
