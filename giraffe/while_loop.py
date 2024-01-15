i = 0
while i <= 10:
    print(i)
    i += 1

secret_word = "giraffe"
guess = ""
hint = ""
i = 0
while guess != secret_word and i < len(secret_word):
    print(i)
    print(len(secret_word))
    print(hint)
    guess = input("Enter the word: ")
    if(len(hint) == 0): 
        hint = "No, here is the hint for you: "
    hint += secret_word[i]
    i += 1

if i == len(secret_word):
    print("You lost")
else: 
    print("Yo win!")

    