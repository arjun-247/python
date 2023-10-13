# import random
# l=[1,2,3,4,5,6,7]
# m=random.choice(l)
# print(m)


# import random
# list=['rock','paper','scissor']
# r=random.choice(list)
# n=input("enter rock,paper,scissor:")
# if r==list[0] and n==list[1]:
#     print(n,"vs",r)
#     print("paper wins")
# elif r==list[1] and n==list[1]:
#     print(n,"vs",r)
#     print("tie")
# elif r==list[2] and n==list[1]:
#     print(n,"vs",r)
#     print("sccissor wins")
# elif r==list[0] and n==list[0]:
#     print(n,"vs",r)
#     print("tie")
# elif r==list[1] and n==list[0]:
#     print(n,"vs",r)
#     print("paper wins")
# elif r==list[2] and n==list[0]:
#     print(n,"vs",r)
#     print("rock wins")
# elif r==list[0] and n==list[2]:
#     print(n,"vs",r)
#     print("rock wins")
# elif r==list[1] and n==list[2]:
#     print(n,"vs",r)
#     print("scissor wins")
# elif r==list[2] and n==list[2]:
#     print(n,"vs",r)  
#     print("tie")
# else:
#     print("enter valid choice")


# import random

# # List of fruits
# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# # Randomly select a fruit from the list
# selected_fruit = random.choice(fruits)

# # Initialize variables
# max_chances = 5
# chances_left = max_chances
# guessed_word = ["_"] * len(selected_fruit)

# print("Welcome to the Fruit Guessing Game!")
# print("You have 5 chances to guess the fruit letter by letter.")

# while chances_left > 0:
#     # Display the current state of the guessed word
#     print(" ".join(guessed_word))

#     # Get a letter guess from the user
#     letter_guess = input("Guess a letter: ").lower()

#     if len(letter_guess) != 1 or not letter_guess.isalpha():
#         print("Please enter a single letter.")
#         continue

#     if letter_guess in selected_fruit:
#         for i in range(len(selected_fruit)):
#             if selected_fruit[i] == letter_guess:
#                 guessed_word[i] = letter_guess
#         if "".join(guessed_word) == selected_fruit:
#             print("Congratulations! You guessed the fruit: " + selected_fruit)
#             break
#     else:
#         chances_left -= 1
#         print(f"Wrong guess. {chances_left} {'chance' if chances_left == 1 else 'chances'} left.")

# if chances_left == 0:
#     print(f"Sorry, you're out of chances. The fruit was '{selected_fruit}'.")

import random
list=['apple','apple','apple']
f=random.choice(list)   
chance=5
chances=chance
word=["_"] * len(f)
while chances > 0:
    print(" ".join(word))
    n=input("guess the fruit:")
    if len(n)!=1 or not n.isalpha():
        print("enter single letter")
        continue
    if n in f:
        for i in range(len(f)):
            if f[i]==n:
                word[i]==n
        if "".join(word)==f:
            print("correct")
            break
    else:
        chances=chances-1
        print("chance left",chances)

if chances==0:
    print("out of chances")