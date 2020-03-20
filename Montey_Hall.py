import random
import time

#ask=input('Do you want to play Monty Hall game[u] or run simulation[s]?')
ask='u'
if ask=='u':
	door=[]
	car_door = random.randint(0,3)

	for i in range(3):
		if i==car_door:
			door.append(1)
		else:
			door.append(0)

	print('There are 3 doors and behind one is a luxury car and behind others are goats')
	door_select=int(input('Select a door! :-'))
	if door[door_select-1]==1:
		ch=random.randint(0,2)
		l=0
		for i in range(3):
			
			if i!=door_select-1 and door[i]!=1 and l==ch:
				print('Door {} has a goat behind it!'.format(i+1))
			elif i!=sd-1 and door[i]!=1 and l!=ch:	
				switch_option=i
			
			l+=1
			
	else:
		for i in range(3):

			if i!=door_select-1 and door[i]!=1:
				print('Door {} has a goat behind it!'.format(i+1))
				
			elif i!=door_select-1:
				switch_option=i

				
		
	a=input('Do you want to switch your door now?[y/n]')
	if a=='y':
		door_select=switch_option+1
		if door[switch_option]==1:
			result=1
		else:
			result=0
	elif a=='n':
		if door[door_select-1]==1:
			result=1
		else:
			result=0
	print('Lets see what is behind your door')
	for i in range (5):
		print('.')
		time.sleep(0.4)

	if result==1:
		print('Behind door {} is the car!!!!. Congrats you won'.format(door_select))
	else:
		print('Behind door {} is a goat!!!!. Better luck next time'.format(door_select))

