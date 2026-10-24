#57-->smart canteen order
rice=20
eggs=30
noodles=10
chicken=2000
items=['fried rice','noodles','chicken rice']
special=['eggs','chicken']
print("available items are: ")
for i in items:
    print(i)
print("additional:")
for i in special:
    print(i)
nxt_order=1
while nxt_order!="no":
    if rice<1 or eggs<1 or noodles<1 or chicken<200:
        nxt_order=0
        print("out of stock")
        break
    order=input("what you want to order: ").lower()
    extra=input("specialization?(0 if no need): ").lower()
    if order=="fried rice":
        rice=rice-1
        if extra=="egg":
            eggs=eggs-1
        elif extra=="chicken":
            chicken=chicken-200
    elif order=="chicken rice":
        rice=rice-1
        if extra=="egg":
            eggs=eggs-1
    elif order=="noodles":
        noodles=noodles-1
        if extra=="egg":
            eggs=eggs-1
        elif extra=="chicken":
            chicken=chicken-200
    else:
        print("there no such type of item")
    nxt_order=input("do you want next order('no' if dont need): ")