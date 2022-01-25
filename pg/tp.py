# Var values: dic {index(int): value(int)}
n = 8
barre = list(range(n))
values = {
    0: 0,
    1: 2,
    2: 3,
    3: 8,
    4: 10,
    5: 13,
    6: 15,
    7: 16,
    8: 12
}

# Get all subBarre and gain
subBarre = {}
for i in range(n+1):
    for j in range(i + 1, n + 1):
        subBarre[str(barre[i:j])] = 0 
        
# Calculate gain for each subBarre
for i in range(len(subBarre)):
    barreFrame = list(subBarre)[i]
    price = 0
    for y in range(len(barreFrame)):
        price += values[y]
    print(price)