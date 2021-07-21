import random

#global variable
correct = "Congratulations "
wrong_msg = "Oops wrong guess!!"
game_over = "oops Game Over"

random_number = random.randint(1, 10)


def play():
  # global calling
	global wrong_msg, game_over, correct, andom_number
	#
	
  # attemets and limit
	guess_limit = 6
	start = 0
  
	print(random_number)
	while start < guess_limit:
		guess = int(input("Guess a number from 1 to 10: "))
		start += 1
		if guess != random_number:
			print(wrong_msg)
      print(start)
		elif guess == random_number:
			print(correct)
      print(start)
		...

	print(game_over)

play()
