import csv



with open('softwareDev34/Unit3/AOS1/practiceSACs/members.csv', newline='') as f:
    reader = csv.reader(f, skipinitialspace=True)
    first_row = reader.__next__()          # first row
    next(reader)          # first row
    second_row = next(reader)
print(first_row)
print(second_row)