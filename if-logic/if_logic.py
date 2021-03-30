#!/usr/bin/env python3
""" Author: Jeffrey Moreta """
# importing the questions from the quiz
from quiz import sorting_hat as quiz


# for visual space
def spacer():
    print("\n")


# specifies if the input is allowed
def is_valid(response):
    valid_answers = ["A", "B", "C", "D"]
    return response.upper().strip() in valid_answers


# display the question to the user
def display_question(response):
    print(quiz.get(response).get("question"))


# display all the answers for the questions
def display_answers(response):
    for show_answer in quiz.get(response).keys():
        if show_answer.startswith("answer"):
            print(quiz.get(response).get(show_answer))


def display_result(response):
    # max possible result = 679
    if response >= 670:
        print("Slytherin")

    elif response >= 665:
        print("Huggle Puff")

    elif response >= 660:
        print("Raven Claw")

    elif response >= 655:
        print("Griffondor")
    # min possible result = 650
    else:
        print("Muggle")


def main():
    # this list will hold the values of all the user's answers
    answers = []

    # loop through all the questions in the quiz
    for quizlet in quiz.keys():

        display_question(quizlet)           # displays the question
        display_answers(quizlet)            # displays all the potential answers
        spacer()

        # ask user for their answer
        answer = input("What's your choice? (A, B, C, D)\t")

        # make sure the user's answer is allowed
        while not is_valid(answer):
            print("\nAnswer wasn't valid. Please try again")
            answer = input("What's your new choice? (A, B, C, D)\t")

        # push the number value of the answer in to a list
        # this will help us create an end result
        # ord converts an ASCII value into an int
        answers.append(ord(answer.upper()))

    # display survey results
    display_result(sum(answers))


if __name__ == "__main__":
    main()
