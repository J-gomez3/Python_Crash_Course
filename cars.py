cars=['Bmw','Honda','Mitsubishi', 'Alfa_Romeo','Mclaren']
print("Here is the original list")
print(cars)
print("\nHere are the sorted cars")
print(sorted(cars))											   #Sorts list in alphabetical order
print("\n Here is the reverse sorted cars")
cars.sort(reverse=True)										   #Sorts list in reverse alphabetical order
print(cars)
cars.reverse()                                                 #Reverse the list from end to beginning 
print(cars)
print(len(cars))                                                      #lenght of list