try:
    import random

    count =0
    limit = 3
    secret_number = random.randint(1,1)
    scores = 15
    total_gussing_num = 10

    while count < limit:
        Guess = int(input("Enter number from 1 to 10 "))
        count += 1

        if Guess < secret_number:
            print(f"you Guessed {Guess} and it's a low number ")
            left = limit - count
            print(f"{count} Gone left with {left}")
            if left == 0:
                print("Game Over".upper())
        elif Guess > total_gussing_num:
            print("Oops out of range")
            left = limit - count

            if left == 0:
                print(f"game over".upper())

        elif Guess > secret_number:
            print(f"You Guessed {Guess} which is wrong and higher...")
            left = limit - count
            print(f"{count}Gone Left with {left}")
            if left == 0:
                print("GAME OVER")
        elif Guess == secret_number:
            left = limit - count
            score_cal = scores - count
            print(f"You Guessed {Guess} which is Correct score {score_cal} ")
            print(f"you tried {count}x and left with {left}")
            print("")

            if left > 1:
                level2_or_stop = input(f"Do you want to keep playing with you last chances? (YES)Y / (NO)N: ").lower()
                print("")
                if level2_or_stop == "n":
                    print(f"Thank you for trying our Game..")
                    print(f"Have an nice day ")
                    print(f"Don't forget to learn every day")
                    break
                elif level2_or_stop == "y":
                    over_range = 1  # don't allow user to go below 0
                    over_range_high = 6  # limit user input to 6
                    scores2 = 25
                    start = 0
                    end = 3

                    while end > start:
                        secret_code = random.randint(1,1)  # update every time you fail
                        Guess_2 = int(input("Enter number from 1 to 6 "))
                        start += 1

                        # Stop Over Range (made it first so that it check if it's not what we don't want if not continue scanning)
                        if Guess_2 < over_range:
                            left = start - end  # attempts
                            print(f"Over range choose from 1 to 6 exclude <0")
                            print(f"if you do it again you won't continue. playing")
                            print(f"you tried {start}x and left with {left}")
                            break
                            # add while loop to stop the game if user keeps repeating the same number

                        elif Guess_2 > over_range_high:
                            left = start - end  # attempts
                            print(f"Over range choose from 1 to 6 exclude >7 ")
                            break
                        # Ends

                        elif Guess_2 < secret_code:
                            left = end - start  # attempts
                            print(f"Wrong try again. ur Answer {Guess_2} low. secret num was {secret_code}")
                            print("")
                            print(f"{start} used  and left with {left}")

                        elif Guess_2 > secret_code:
                            left = end - start  # attempts
                            print(f"Wrong try again. ur Answer {Guess_2} high. secret num was {secret_code}")
                            print("")  # spaces
                            print(f"{start} used and left with {left}")

                        elif Guess_2 == secret_code:
                            results = (scores2 - start) + score_cal  # score_cal first step result and scores2 are
                            # new result for level 2
                            # just having problem with updating the result when you keep winning instead they Decrease
                            left = end - start  # attempts
                            print(f"Congratulations you won {results}")#
                            print("")  # spaces
                            print(f"{start} used and left with {left}")

                            if left == 0:
                                print("")# spaces
                                repeat = input("Do you want to continue playing yes or no ").lower()

                                if repeat == "yes":
                                    print("Enjoy")
                                    continue
                                elif repeat == "no":
                                    print(f"Thank you for trying our Game..")
                                    print(f"Have an nice day ")
                                    print(f"Don't forget to learn every day")
                                    break
                                    exit()
                                else:
                                    print("Thank you enjoy your day")

                else:
                    print("Oops Unidentified")
            elif left == 0:
                print("")
                print("Oops you can't continue playing, you don't have enough points.")
                print("")
                rate = input("Did you enjoy? yes or no ").lower()
                if rate == "yes":
                    print("try play again. will keep making you happy ")
                elif rate == "no":
                    print("Ooops sorry...")


except ValueError:
        print("please Enter a number not a latter...")
except TypeError:
    print("Please Enter a number not a alphabet")
