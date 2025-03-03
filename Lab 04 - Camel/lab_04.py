import random


def main():
    print("Here are instructions for the game")

    thirst = 0
    miles_traveled = 0
    horse_tiredness = 0
    miles_gangsters_traveled = -20
    drinks_in_canteen = 3

    done = False

    while not done:
        print("A.Drink from your canteen.")
        print("B.Ahead moderate speed.")
        print("C.Ahead full speed.")
        print("D.Stop for the night.")
        print("E.Status check.")
        print("Q.Quit.")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            done = True
            print("GAME OVER")

        elif user_choice.upper() == "E":
            print(miles_traveled)
            print(drinks_in_canteen)
            print(miles_gangsters_traveled)

        elif user_choice.upper() == "D":
            print("The Camel is happy")
            print(horse_tiredness)
            miles_gangsters_traveled += random.randint(7, 14)
            print(miles_gangsters_traveled)

        elif user_choice.upper() == "C":
            miles_traveled += random.randint(10, 20)
            thirst += 1
            print(thirst)
            print(miles_traveled)
            horse_tiredness += random.randint(1, 3)
            print(horse_tiredness)
            miles_gangsters_traveled += random.randint(7, 14)
            print(miles_gangsters_traveled)

        elif user_choice.upper() == "B":
            miles_traveled += random.randint(5, 12)
            print(miles_traveled)
            thirst += 1
            print(thirst)
            horse_tiredness += 1
            print(horse_tiredness)
            miles_gangsters_traveled += random.randint(7, 14)
            print(miles_gangsters_traveled)

        elif user_choice.upper() == "A":
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
                print(drinks_in_canteen)
                thirst = 0
                print(thirst)
            else:
                print("ERROR")
            if thirst > 6:
                print("You died of thirst!")
                done = True
            elif thirst > 4:
                print("You are thirsty.")

            if horse_tiredness > 8:
                print("Your camel is dead.")
                done = True
                break
            elif horse_tiredness > 5:
                print("Your camel is getting tired")

            if miles_gangsters_traveled < 0:
                print("The natives have caught you! GAME OVER.")
                done = True
            if miles_gangsters_traveled < 15:
                print("The natives are getting close!")

            if miles_traveled >= 200:
                print("Congrats! You won after traveling {distance_travelled} miles!")


main()