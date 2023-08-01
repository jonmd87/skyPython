# 1 get name of user and save
# 2 get words from file words.txt
# 3 shuffle the list of words
# 4 pop word from list of words while words in list
# 5 shuffle letters in this word
# 6 display this shuffle word
# 7 suggest to user guess the word
# 8 if user guess this word
#           give him one point
# 9 go to step 4
import random


def get_name():
    name = ''
    print("Hello this is game 'Guess the word'\nLet's start")
    while name is None or 1 > len(name):
        name = input("Please enter your name: ")

    return name


def get_words_from_file():
    with open("words.txt") as file:
        return file.read().split('\n')


def guess_word(word):
    points = 3
    temp = list(word)
    random.shuffle(temp)
    answer = ''
    while points != 0 and answer != word:
        points -= 1
        answer = input(f"guess this word [{temp}]: ")
    return points


def write_score_in_file(line):
    with (open('history.txt', "a")) as file:
        file.writelines("".join(line))
        file.writelines('\n')


score = 0
name = get_name()
words = get_words_from_file()
random.shuffle(words)

while len(words) > 0:
    point = guess_word(words.pop())
    if point > 0:
        score += point
        print("you guessed this word")
    else:
        print("You loose.")
    if len(words) > 1:
        print("next try")

print(f"Hey, {name} your score = {score}")

write_score_in_file((name, str(score)))
