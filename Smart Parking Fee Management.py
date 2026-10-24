#15-->parking fees
A=["car",'bike','truck','bicycle']
print(f'available slots for vehicles {A}')
parking_vehicle=input("enter your parking vehicle: ").lower().strip()
time=int(input("enter how many hours(0 if less than 1 hour): "))
if parking_vehicle =='car':
    maximum=10
    fee=100
elif parking_vehicle =='bike':
    maximum=5
    fee=50
elif parking_vehicle =='truck':
    maximum=15
    fee=200
else:
    maximum=0
    fee=0
if time>maximum:
    print(f'you need to pay extra 1000')
else:
    for i in range(time):
        fee=fee+20*(fee/100)
print(f'your total fee is {int(fee)}')
