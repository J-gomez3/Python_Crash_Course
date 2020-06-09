requested_toppings=[]
#for requested_topping in requested_toppings:
#	if requested_topping == 'green peper':
#		print("Sorry we are out of green peper")
#	else:
#		print(f"adding {requested_topping}")
if requested_toppings:
	for requested_topping in requested_toppings:
			print(f"adding {requested_topping}")
			print("\nFinished making your pizza")
else:
			print("are you sure you want a plain pizza?")