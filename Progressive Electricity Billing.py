#2-->electricity bill calculation
n = int(input("Enter number of households: "))
bills = []
for i in range(n):
    print("Household", i + 1)
    name = input("Enter household name: ")
    units = float(input("Enter electricity units consumed: "))
    if units <= 100:
        bill=units*2
    elif units<=200:
        bill= units*3
    elif units<=300:
        bill=units*5
    else:
        bill=units*7
    fixed_charge=50
    total_bill=bill+fixed_charge
    bills.append([name, units, total_bill])
for i in bills:
    print("Household:", i[0])
    print("Units consumed:", i[1])
    print("Energy charge: Rs.", i[2] - 50)
    print("Fixed charge: Rs. 50")
    print("Total bill: Rs.", i[2])
highest=bills[0]
for j in bills:
    if j[2]>highest[2]:
        highest=j
print("Highest bill:", highest[0])
print("Amount: Rs.", highest[2])
