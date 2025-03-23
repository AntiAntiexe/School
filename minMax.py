x = [1,9,20,56,23,89,77,64,40,200]

def maximum(vals):
    Max = 0
    for item in vals:
        if item > Max:
            Max = item
    return(Max)

def minimum(vals):
    mini = vals[0]
    for item in vals:
        if item < mini:
            mini = item
    return(mini)
print('Maximum:', maximum(x))
print('Minimum:', minimum(x))

x = max()


    