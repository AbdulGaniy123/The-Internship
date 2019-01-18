import random
count = 0
while (count < 5):
    number = random.randint(1,201)
    guess_number = input("Guess a number :")
    val = int(guess_number)
    if(val > number):
        print(number)
        print("try again, you are higher than the number")
        count += 1
        if (count == 5):
            print("You tried 5 times, you have exceeded the number of trials")

    elif(number > val):
        print(number)
        print("try again, you are lower than the number")
        count += 1
        if (count == 5):
            print("You tried 5 times, you have exceeded the amount of trials ")
    elif(val == number):
        print(number)
        print("you are correct")
        count += 1
        if (count == 1):
            print("you are so lucky, you got it at first guess ")
        elif (count == 2):
            print("you got it at the second guess")
        elif (count == 3):
            print("you got it at the third guess")
        elif(count == 4):
            print("you got it at the fourth guess")
        elif(count == 5):
            print("you got it at your last guess")
