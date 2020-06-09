#alien_0={'color': 'green', 'points': 5}
#print(alien_0['color'])
#print(alien_0['points'])
#new_points=alien_0['points']
#print(f"You just earned {new_points} Points!")
#print(alien_0)
#alien_0['x_position']=25
#alien_0['y_position']=5
#print(alien_0)
#alien_0={}
#alien_0['color']='green'
#alien_0['points']=25
#print(f"the aliens color is {alien_0['color']}")
#alien_0['color']= 'yellow'
#print(f"Then new aliens color is {alien_0['color']}")
alien_1={'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_1['x_position'], alien_1['y_position']}")

#Move alien to the right
#Determine how far to move the alien based on it current speed.
if alien_1['speed'] == 'slow':
	x_increment = 1
elif alien_1['speed'] == 'medium':
	x_increment = 2
else:
	#this must be a fast alien
	x_increment = 3

#The position is the old position plus the increment 
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position: {alien_1['x_position'], alien_1['y_position']}")
del alien_1['y_position']
print(alien_1)