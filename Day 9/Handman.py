import random

# Programming languages list
word_list = [
    "python", "java", "javascript", "html", "swift",
    "c", "cplusplus", "csharp", "ruby", "rust",
    "go", "kotlin", "php", "sql", "typescript",
    "bash", "perl", "r", "dart", "scala",
    "haskell", "matlab", "fortran", "assembly"
]

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("Guess the Programming Language!")
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
        
    print(display)

    if guess not in chosen_word:
        lives -= 1  
        print(f"Wrong. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lose. The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print("You win! The word was:", chosen_word)
