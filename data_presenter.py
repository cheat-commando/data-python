cupcakes = open('CupcakeInvoices.csv').readlines()

for line in cupcakes:
    print(line)

for line in cupcakes:
    print(line.split(',')[2])

total = 0

for line in cupcakes:
    first, last, flavor, amount, unit_cost = line.split(',')
    real_amount = int(amount)
    real_cost = round(float(unit_cost))
    total += real_cost*real_amount
    print("Total rounded cost for",first,last,"is $",real_cost*real_amount)

print("The total is:",total)

cupcakes.close()

