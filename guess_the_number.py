import random
import time
import sys
guesses=10
number=random.randint(1,100)
def play():
	print("Welcome to guess the number.")
	while True:
		time.sleep(0.005)
		if guesses<=0:
			print("Sorry, but you are out of guesses.")
			print("The number was "+number)
			print("Press enter to exit.")
			input()
			sys.exit()
		try:
			print("You currently have "+guesses+" "+plural(guesss,"guess","guesses")+" left.")
			print("Enter a guess (from 1 to 100)")
			guess=int(input())
			if guess>100:
				print("Out of range.")
				continue
			elif guess<1:
				print("Out of range.")
			elif guess<number:
				guesses-=1
				print("That's too low.")
			elif guess>number:
				guesses-=1
				print("That's too high.")
			else:
			
				print("You got it! The number was "+number+".")
				print("You had "+guesses+" "+plural(guesss,"guess","guesses)+" left.")
				print("Press enter to exit.")
				input()
				sys.exit()
		except:
			print("There was an error.")
			continue
def plural(number,first_option,second_option)
	if number==1 or number==-1:
		return first_option
	else:
		return second_option
if __name__=="__main__":
	play()
