

print("Welcome")

secret_name = "coding"
secret_name2 = "python"
correct1 = "Learning to coding it's the best thing you could ever do in your life. learn Python "
full = "Learning to coding it's the best thing you could ever do in your life. learn Python "


# Hide secret code
def show_screen():
    
    print("Learning to ______ it's the best thing you could ever do in your life. learn ______ ")


# Hide secret code after give secret number 1
def second_level():
    print("Learning to coding it's the best thing you could ever do in your life. learn _______")


# Show the everything after correct attempts
def show_full():
    global full
    print(full)


# Start Game
def play():
    # Global calling
    global secret_name, correct1, full
    #

    # Starting point and ending point variables
    attempts = 0
    limit = 3
    #
    while attempts < limit:
        # hide the code first
        show_screen()
        print()

        # none Case sensitive
        guess_name = input("Enter a guess name: ").lower()
        attempts += 1
        
        if guess_name == secret_name:
            second_level()

            # how attempts so far
            print(f"{attempts} attempts")
            print("")

            if attempts == limit:
                print("You Guessed 1 Question only try again next time to answer all")
                break
            else:
                # Level 2
                while attempts < (limit+1):
                    # revel the first answer and hide the last one
                    second_level()
                    guess_name = input("Enter a guess 2: ").lower()
                    attempts += 1

                    if guess_name == secret_name2:
                        show_full()
                        print(f"{attempts} attempts")
                        print("")
                        exit()

                    elif guess_name != secret_name:
                        print("incorrect.")
                        print("")
                        print(f"{attempts} attempts")
                    elif attempts == 3:
                        print("Game Over...")

        elif guess_name != secret_name:
            print("incorrect...")
            print(f"{attempts} attempts")
            if attempts == 3:
                print("Game Over...")


play()
