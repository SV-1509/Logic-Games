import random
import time

ask=input('Do you want to play Monty Hall game[u] or run simulation[s]?')

if ask=='u':
	door=[]
	car_door = random.randint(0,2)
	#print(car_door)
	for i in range(3):
		if i==car_door:
			door.append(1)
		else:
			door.append(0)
	#print(door)
	print('There are 3 doors and behind one is a luxury car and behind others are goats')
	door_select=int(input('Select a door! :-'))
	if door[door_select-1]==1:
		ch=random.randint(0,1)
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
elif ask=='s':
	n=int(input('How many iterations do you want the simulation to run :-'))
	switching=input('Do you switch everytime or never [e/n] :-')
	win=0
	lose=0
	for t in range(n):
		
		door=[]
		
		car_door = random.randint(0,2)
		door_select = random.randint(0,2)
		#print(car_door)
		#print(door_select)
		for i in range(3):
			if i==car_door:
				door.append(1)
			else:
				door.append(0)
		if door[door_select]==1:
			ch=random.randint(0,1)
			l=0
			for i in range(3):
				
				if i!=door_select and door[i]!=1 and l==ch:
					switch_option=i
				l+=1		
		else:
			for i in range(3):

				if i!=door_select and door[i]==1:
					switch_option=i
		
		if switching=='e':
			door_select=switch_option
			if door[switch_option]==1:
				result=1
			else:
				result=0
		elif switching=='n':
			if door[door_select]==1:
				result=1
			else:
				result=0
		if result==1:
			win+=1
		else:
			lose+=1
	win_percent=win*100/n
	lose_percent=lose*100/n
	print('Out of {} game:'.format(n))
	print('No of Wins: {} ; Win% = {}'.format(win,win_percent))
	print('No of Losses: {} ; Lost% = {}'.format(lose,lose_percent))



