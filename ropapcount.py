import random
a={1:'r',2:'p',3:'s'}
s1=0
s2=0
while(True):
	p=input("your choice r/p/s: ")
	c=a[random.randint(1,3)]

	print("you choose",p,"computer choose",c)
	if(p=='r' or p=='p' or p=='s'):
		if(p==c):
			print("tie")
		elif((p=='r'and c=='p') or (p=='p' and c=='s') or (p=='s' and c=='r')):
			s1=s1+1
			print("computer won",s1,"times")
		else:
			s2=s2+1
			print("you won",s2,"times")
	else:
		print("give proper input")
		break
	if(s1==3 or s2==3):
		if(s1==3):
			print("i'm sorry,computer won the game")
		else:
			print("congrats u won against computer,have a great day")
		break	