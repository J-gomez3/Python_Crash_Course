guest= ['Yon','Kio', 'Yomi']
print(f"would you like to come for dinner {guest[0].title()}?")
print(f"would you like to come for dinner {guest[1].title()}?")
print(f"would you like to come for dinner {guest[2].title()}?")
guest_not_making_it = guest.pop(1)
print(f"{guest_not_making_it} can't come to dinner")
guest.insert(1,'Deya')
print(f"{guest_not_making_it} couldn't come over so we invited {guest[1]}")
print(f"would you like to come for dinner {guest[0].title()}?")
print(f"would you like to come for dinner {guest[1].title()}?")
print(f"would you like to come for dinner {guest[2].title()}?")
print(f"{guest[0]} {guest[1]} and, {guest[2]} I just found a bigger table with the capacity for 3 more")
guest.insert(0,'Julian')
guest.insert(2, 'Janiel')
guest.append('Mamajuana')
print(f"would you like to come for dinner {guest[0].title()}?")
print(f"would you like to come for dinner {guest[1].title()}?")
print(f"would you like to come for dinner {guest[2].title()}?")
print(f"would you like to come for dinner {guest[3].title()}?")
print(f"would you like to come for dinner {guest[4].title()}?")
print(f"would you like to come for dinner {guest[5].title()}?")