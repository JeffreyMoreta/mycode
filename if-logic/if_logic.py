#!/usr/bin/env python3
""" Author: Jeffrey Moreta """
# importing the questions from the quiz
from quiz import sorting_hat as quiz


# specifies if the input is allowed
def is_valid(user_response):
    valid_answers = ["A", "B", "C", "D"]
    return user_response.upper().strip() in valid_answers


# asks the user for their answer
def user_input():
    return input("What's your choice? (A, B, C, D)\t")


# display the question to the user
def display_question(quizlet_question):
    print(quiz.get(quizlet_question).get("question"))


# display all the possible answers for the questions
def display_answers(quizlet_question):
    for potential_answer in quiz.get(quizlet_question).keys():
        if potential_answer.startswith("answer"):
            print(quiz.get(quizlet_question).get(potential_answer))
    print("\n")


# ask user for their answer
def ask_response():
    answer = user_input()

    # make sure the user's answer is allowed
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

        display_question(quizlet)               # displays the question
        display_answers(quizlet)                # displays all the potential answers
        answer = ask_response()                 # ask user for response
        answers.append(ord(answer.upper()))     # ord converts an ASCII value into an int

    # display survey results
    display_result(sum(answers), len(quiz))


if __name__ == "__main__":
    main()
