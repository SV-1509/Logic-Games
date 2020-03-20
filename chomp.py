import random

chomp=[0,1,2,3,4,5]
s1=[1,2,3,4,5]
s2=[1,3,4,1,3,4]
s3=[1,2,3,1,2,3]
s4=[1,2,1,2]
s5=[1,3,1,3]
sa=[1,2,1,2]
rem=[]
u=[]
s=0
def state1():
	global s1,u
	if s1==[]:

		s1=[1,2,3,4,5]
	return s1[random.randint(0,len(s1)-1)]
def state2():
	global s2
	if s2==[]:
		s2=[1,3,4]
	return s2[random.randint(0,len(s2)-1)]
	
def state3():
	global s3
	if s3==[]:
		s3=[1,2,3]
	return s3[random.randint(0,len(s3)-1)]
	
def state4():
	global s4
	if s4==[]:
		s4=[1,2]
	return s4[random.randint(0,len(s4)-1)]
	
def state5():
	global s5
	if s5==[]:
		s5=[1,3]
	return s5[random.randint(0,len(s5)-1)]
	
def state6():
	return 1
def state7():
	return 3
def statea():
	return sa[random.randint(0,len(sa)-1)]
def state():
	global chomp,rem,s
	
	if chomp==[0,1,2,3,4,5]:
		s=int(state1())
		rem.append(1)
	if chomp==[0,1,3,4]:
		s=int(state2())
		rem.append(2)
	if chomp==[0,1,2,3]:
		s=int(state3())
		rem.append(3)
	if chomp==[0,1,2]:
		s=int(state4())
		rem.append(4)
	if chomp==[0,1,3]:
		s=int(state5())
		rem.append(5)
	if chomp==[0,1]:
		s=int(state6())
	if chomp==[0,3]:
		s=int(state7())
	if chomp==[0,1,2,3,4]:
		s=int(statea())
	return s	
def new_state(i):
	global chomp
	
	if chomp==[0,1,2,3,4,5]:
		if i==1:
			chomp=[0,3]
		elif i==2:
			chomp=[0,1,3,4]
		elif i==3:
			chomp=[0,1,2]
		elif i==4:
			chomp=[0,1,2,3]
		elif i==5:
			chomp=[0,1,2,3,4]
		

	elif chomp==[0,1,3,4]:
		if i==1:
			chomp=[0,3]
		elif i==3:
			chomp=[0,1]
		elif i==4:
			chomp=[0,1,3]
		

	elif chomp==[0,1,2,3]:
		if i==1:
			chomp=[0,3]
		elif i==2:
			chomp=[0,1,3]
		elif i==3:
			chomp=[0,1,2]
		


	elif chomp==[0,1,2]:
		if i==1:
			chomp=[0]
		elif i==2:
			chomp=[0,1]
		

	elif chomp==[0,1,3]:
		if i==1:
			chomp=[0,3]
		if i==3:
			chomp=[0,1]
		
	

		

	elif chomp==[0,1,2,3,4]:
		if i==1:
			chomp=[0,3]
		elif i==2:
			chomp=[0,1,3,4]
		elif i==3:
			chomp=[0,1,2]
		elif i==4:
			chomp=[0,1,2,3]

	elif chomp==[0,3]:
		chomp=[0]

	elif chomp==[0,1]:
		chomp=[0]

def ai_win():
	global rem,s1,s2,s3,s4,s5,u
	
	for ai in range(0,len(rem),2):
		if rem[ai]==1:
			
			for p in range(2):
				s1.append(rem[ai+1])
			
		if rem[ai]==2:
			for p in range(2):
				s2.append(rem[ai+1])

		if rem[ai]==3:
			for p in range(2):
				s3.append(rem[ai+1])
		if rem[ai]==4:
			for p in range(2):
				s4.append(rem[ai+1])
		if rem[ai]==5:
			for p in range(2):
				s5.append(rem[ai+1])
	rem=[]

def ai_lose():
	global rem,s1,s2,s3,s4,s5

	for ai in range(0,len(rem),2):
		if rem[ai]==1:
			s1.remove(rem[ai+1])
		if rem[ai]==2:
			s2.remove(rem[ai+1])
		if rem[ai]==3:
			s3.remove(rem[ai+1])
		if rem[ai]==4:
			s4.remove(rem[ai+1])
		if rem[ai]==5:
			s5.remove(rem[ai+1])
	rem=[]		
		

game=1

move=0
win=0
lost=0
while game<=100000:
	#print(s1)

	r='y'
	move+=1
	if move%2==0:
		if chomp!=[0]:
			#print(chomp)
			#print('Move {} - User'.format(move))
			a=chomp[random.randint(1,len(chomp)-1)]
			#print(a)
			#a= int(state())
			new_state(a)

		else:
			if game%1000==0:
				print('AI won {}/{} .................. {}'.format(win,game,win*100/game))
			win+=1
			ai_win()


			#r=input('Want to play next game?[y/n]')
			if r=='n':
				game=0
			else:
				chomp=[0,1,2,3,4,5]
				game+=1
				move=0

	else:
		if chomp!=[0]:
			#print(chomp)
			#print('Move {} - Computer'.format(move))
			a= int(state())
			#print(a)
			if len(rem)%2!=0:
				rem.append(a)
			#print(rem)
			new_state(a)

		else:
			if game%1000==0:
				print('AI lost {}/{} ..................{}'.format(lost,game,win*100/game))
			lost+=1
			ai_lose()
			#r=input('Want to play next game?[y/n]')
			if r=='n':
				game=0
			else:
				chomp=[0,1,2,3,4,5]
				game+=1
				move=0
	
	
print('Win - {}'.format(win))

print('Lost - {}'.format(lost))
print('Final win rate ={}'.format(win*100/game))
	
