import random
import threading

print("Number guessing game")
print("----------------------")
name = input("Enter your name")
print("You only get 4 guesses")
print("First guess wont have a clue")
print("Clues will be given if required by the user")
print("Maximum 2 clues only")
hidden_number = random.randint(1, 50)
cn = 0
Chances = 0
t1 = 0

m: int = 0
print("Start guessing")
print("Number between 1 and 50")

while Chances < 4:
    guess = int(input("Enter your guess"))

    if guess == hidden_number:

        print("Congratulation", name)
        print("YOU WON!!!")
        break
    else:

        print("Wrong")

    n = int(input("Do u want clues(1 for yes 0 for no)"))
    if n == 1:

        m = m + 1
        if m <= 2:
            sq = (hidden_number * hidden_number)
            cq = (sq * hidden_number)
            uv = (((hidden_number / 41) * 369) + 10)
            lds = sq % 10

            ldc = cq % 10

            ld = hidden_number % 10
            #if 1 <= times <= 3:
                #cn = random.randint(1, 4)
            #else:
                #cn = random.randint(4, 5)
            cn = random.randint(1, 5)

            if t1 != cn:

                if cn == 1:
                    print("The last digit of its square is ", lds)
                elif cn == 2:
                    print("Last digit of its cube is", ldc)
                elif cn == 3:
                    print("(((number/41)*369)+10) is", uv)
                elif cn == 4:
                    print("last digit of the number is", ld)


                elif cn == 5:
                    if guess < hidden_number:
                        print("Your guess was too low: Guess a number higher than", guess)

                    else:
                        print("Your guess was too high: Guess a number lower than", guess)
            else :
                cn = random.randint(1, 5)
                if cn == 1:
                    print("The last digit of its square is ", lds)
                elif cn == 2:
                    print("Last digit of its cube is", ldc)
                elif cn == 3:
                    print("(((number/41)*369)+10) is", uv)
                elif cn == 4:
                    print("last digit of the number is", ld)


                elif cn == 5:
                    if guess < hidden_number:
                        print("Your guess was too low: Guess a number higher than", guess)

                    else:
                        print("Your guess was too high: Guess a number lower than", guess)







        else:
            print("no more clues")


    t1 = cn
    Chances = Chances + 1

if Chances >= 4:
    print("YOU LOSE!!! ", name)
    print("The number is", hidden_number)
