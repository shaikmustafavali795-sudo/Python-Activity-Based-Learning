#3-->hospital billing
patients = []
n = int(input("Enter number of patients: "))
for i in range(n):
    print("Enter details for Patient",i+1)
    name = input("Enter patient name: ")
    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))
    total = consultation + diagnostic + treatment
    if total>=10000:
        discount=(total/100)*20
    elif total>=5000:
        discount=(total/100)*10
    else:
        discount=0
    total_bill=total-discount
    if total_bill>=10000:
        category="High Billing"
    elif total_bill >= 5000:
        category="Medium Billing"
    else:
        category = "Low Billing"
    patients.append([name, total, discount, total_bill, category])
for j in patients:
    print("Patient Name:", j[0])
    print("Total Charges: Rs.", j[1])
    print("Concession: Rs.", j[2])
    print("Final Bill: Rs.", j[3])
    print("Classification:", j[4])

print("Total patients processed:", len(patients))
