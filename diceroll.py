import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("press r to roll the dice")
	if(n=='r'):
	 r=myroll()
	 count=count+r
	 print("u got",r)
	 print("new position is",count)
	 if(count==8):
	 	count=37
	 	print("i got the ladder")
	 elif("count==11"):
	 	count=2
	 	print("sorry,u got the snake")
	 elif(count==13):
	 	count=34
	 	print("i got the ladder")
	 elif(count==25):
	 	count=4
	 	print("sorry,u got the snake")
	 elif(count==38):
	 	count=9
	 	print("sorry,u got bit by the snake")
	 elif(count==40):
	 	count=68
	 	print("yayy,u got the ladder")
	 elif(count==52):
	 	count=81
	 	print("woah,u got the ladder")
	 elif(count==65):
	 	count=46
	 	print("ohh,u got bitten by the snake")
	 elif(count==76):
	 	count=97
	 	print("congo,u got the ladder")
	 elif(count==89):
	 	count=70
	 	print("sry,got bitten by the snake")
	 elif(count==93):
	 	count=64
	 	print("got bitten by the snake")
	 elif(count>=100):
	 	print("you won the game")

				

