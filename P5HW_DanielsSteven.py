# corrected spelling of "Congradulations" along with a couple of other spelling/grammar issues
# actually used functions
import random
def main():
    again = "y"
    print("Welcome to Math Quiz\n")
    while again == "y":
        display_menu()
        number1 = random.randint(10,99)
        number2 = random.randint(10,99)
        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            addition(number1, number2)
        elif choice == '2':
            subtraction(number1, number2)
        elif choice == '3':
            again="n"
        else:
            print("Invalid option")
    print("Thank you for playing...")
    print("Bye!!")

def display_menu():
    print("\nMAIN MENU    ")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")

# write your functions here
def addition(num1, num2):
    print(" ",num1,"\n+", num2)
    answer = num1 + num2
    checkAnswer(answer)

def subtraction(num1, num2):
    print(" ",num1,"\n-", num2)
    answer = num1 - num2
    checkAnswer(answer)

def checkAnswer(answer):
    guessesTaken = 1
    print("\nEnter answer, ")
    guess = int(input())
    while guess != answer:
        if guess < answer:
            print("Sorry, guess is too low. \n")
            guess = int(input("Try again: "))
            guessesTaken +=1 # guessesTaken = guessesTaken + 1
        else:
            print("Sorry, guess is too high. \n")
            guess = int(input("Try again: "))
            guessesTaken +=1 # guessesTaken = guessesTaken + 1
    print("Congratulations!!!! Your answer is correct.")
    print("Number of guesses: ",guessesTaken,sep='')

    

main()
