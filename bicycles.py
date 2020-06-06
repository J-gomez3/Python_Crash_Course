names= ['kio', 'Yon', 'Yomi', 'deya']
message= "I would like to drink today with"
print(f"{message} {names[3].title()}")

names[0]='Luis'
print(f"and, {names[0].title()}")

print(names)
names.append('Gonzalo')
print(names)

motorcycle =[]
motorcycle.append('yamaha')
motorcycle.append('kawasaki')
print(names,"\n", motorcycle)

motorcycle.insert(0,'bmw')
print(motorcycle)

print(motorcycle)
#popped_motorcycle = motorcycle.pop(1)
#print(popped_motorcycle)
#print(f"{message} {names[0]}, also I sold my last motorcycle that was a {popped_motorcycle}. ")
print(motorcycle)
motorcycle.remove('bmw')
print(motorcycle)