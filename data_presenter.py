
cupcakes = open('CupcakeInvoices.csv').readlines()

for line in cupcakes:
    print(line)

for line in cupcakes:
    print(line.split(',')[2])

total = 0
vanilla = 0
chocolate = 0
strawberry = 0

for line in cupcakes:
    first, last, flavor, amount, unit_cost = line.split(',')
    real_amount = int(amount)
    real_cost = round(float(unit_cost))
    if flavor == "Chocolate":
      chocolate += real_cost*real_amount
    elif flavor == "Strawberry":
      strawberry += real_cost*real_amount
    elif flavor == "Vanilla":
      vanilla += real_cost*real_amount
    total += real_cost*real_amount
    print("Total rounded cost for",first,last,"is $",real_cost*real_amount)

print("The total is:",total)

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Chocolate', 'Strawberry', 'Vanilla')
y_pos = np.arange(len(objects))
performance = [chocolate, strawberry, vanilla]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Income $')
plt.title('Income of Cupcake Flavors')

plt.show()

cupcakes.close()
