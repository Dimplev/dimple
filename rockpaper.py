import random

p={1:'r',2:'p',3:'s'}

while True:
	yc=input("YOU CHOOSE: r/p/s: ")
	cc=p[random.randint(1,3)]

	print("computer gave: ",cc)

	if(yc=='r' and cc=='p'):
		print("computer wins the game")
	elif(yc=='s' and cc=='p'):
		print("you win the game")
	elif(yc=='r' and cc=='s'):
		print("you win the game")
	elif(yc=='r' and cc=='p'):
		print("you win the game")
	elif(yc=='p'and cc=='p'):
		print("draw")
	elif(yc=='r' and cc=='r'):
		print("draw")
	elif(yc=='r' and cc=='r'):
		print("draw")
	elif(yc=='s' and cc=='s'):
		print("draw")
	elif(yc=='s' and cc=='r'):
		print("computer wins the game")
	elif(yc=='p' and cc=='s'):
		print("computer wins the game")
		
