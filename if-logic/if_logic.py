#!/usr/bin/env python3
""" Author: Jeffrey Moreta """

# importing the questions from the quiz
from quiz import sorting_hat as quiz


# display the question and all it's answers
def display_quizlet(quizlet):
    # enumerate allows me to use an index, while using a for-loop, and start from where I want
    for index, entry in enumerate(quiz.get(quizlet).keys(), start=1):
        print(quiz.get(quizlet).get(entry))

        # if this is the last potential answer then add an empty line at the end
        if index == len(quiz.get(quizlet)):
            # by default will give a new line - print(end="\n")
            print()


# asks the user for their answer
def user_input():
    return input("What's your choice? (A, B, C, D)\t")


# specifies if the input is allowed
def is_valid(user_response):
    valid_answers = ["A", "B", "C", "D"]
    # returns boolean - if it's in valid_answers or not
    return user_response.upper().strip() in valid_answers


# ask user for their answer
def ask_response():
    answer = user_input()

    # make sure the user's answer is valid
    while not is_valid(answer):
        print("\nAnswer wasn't valid. Please try again")
        answer = user_input()

    return answer


# averages the user's score and assigns house based on most frequent answer picked
def display_result(score, max_questions):
    average = score / max_questions
    # max possible result = 67.9
    if average >= 67.0:
        print("Slytherin")

    elif average >= 66.5:
        print("Hufflepuff")

    elif average >= 66.0:
        print("Raven Claw")

    elif average >= 65.5:
        print("Gryffindor")
    # min possible result = 65.0
    else:
        print("Muggle")


def main():
    # this list will hold the values of all the user's answers
    answers = []

    # loop through all the questions in the quiz
    for quizlet in quiz.keys():

        display_quizlet(quizlet)                # displays all the potential answers
        answer = ask_response()                 # ask user for response
        answers.append(ord(answer.upper()))     # ord converts an ASCII value into an int

    # display survey results
    display_result(sum(answers), len(quiz))


if __name__ == "__main__":
    main()
