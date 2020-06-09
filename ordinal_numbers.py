numbers=[0,1,2,3,4,5,6,7,8,9]
print(numbers)
deleted_numbers=numbers.pop(0)
for number in numbers:
	if number==0:
		print(f"{number}")
	if number==1:
		print(f"{number}st")
	elif number==2:
		print(f"{number}nd")
	elif number==3:
		print(f"{number}rd")
	else:
		print(f"{number}th")