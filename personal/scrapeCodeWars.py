#!/usr/bin/env python3
""" Author | Jeffrey Moreta """

from selenium import webdriver
from bs4 import BeautifulSoup
import info
import os
import time


def kata_template(kata):
    return f"""\
Title:\t {kata.get("title")}
Link:\t {kata.get("link")}
Difficultly:\t {kata.get("difficulty")}
Language:\t {kata.get("language").replace(":", "")}

Solution:
{kata.get("answer")}
"""


def login():
    # activate the chrome browser - allows me to scrape dynamic information
    browser = webdriver.Chrome("./webdrivers/chromedriver")

    # navigate to the login page
    browser.get(info.urls.get("login"))

    # find the login fields
    username = browser.find_element_by_id("user_email")
    password = browser.find_element_by_id("user_password")

    # input personal information
    username.send_keys(info.codeWars.get("username"))
    password.send_keys(info.codeWars.get("password"))

    # click the login button
    browser.find_element_by_tag_name("button").click()

    return browser


# TODO: They use lazy-loading, re-write to pull from their api
def scroll_down():
    # only using ten cycles, proof of concept
    # for cycle in range(1, 11):
    #     # scroll to the bottom of the solutions
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #
    #     # wait until it has scrolled all the way down
    #     time.sleep(0.5)  # in seconds, floats are allowed
    pass


# TODO: Need to pull multiple answers for each kata
def get_attributes(solution):
    # grab the attribute I care about for each solution
    kata_info = {
        "title": solution.find("div", {"class": "item-title"}).find("a").getText(),
        "link": solution.find("div", {"class": "item-title"}).find("a")["href"],
        "language": solution.find("h6").getText(),
        "difficulty": solution.find("div", {"class": "item-title"}).find("div", {"class": "small-hex"}).find(
            "span").getText(),
        "answer": solution.find("div", {"class": "markdown"}).getText()
    }

    return kata_info


def get_solutions(browser):
    # navigate to your solutions
    browser.get(info.urls.get("solutions"))

    scroll_down()

    # grab the raw html of solutions page
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # this will hold our solutions - list[dict, dict, ...]
    # grabbing the information that I care about and adding it to the katas list
    katas = [get_attributes(solution) for solution in soup.findAll("div", {"class": "solutions"})]

    # close the browser
    browser.close()

    return katas


def write_solutions(katas):
    # create the folder that will hold our solutions
    # checks to see if the dir already exists
    if not os.path.exists("./katas"):
        try:
            os.mkdir("./katas")
        except OSError as error:
            print(error)

    # loop through all the solutions
    for solution in katas:
        title = solution.get("title")

        # sanitize the title for illegal characters
        for illegal_char in ["?"]:
            if illegal_char in title:
                title = title.replace(illegal_char, "")

        file_name = title + ".txt"

        # create a file for each solution
        # check to see if the file already exists, if it ask if you want to overwrite it
        # TODO: Create an input that overwrites all files when asked once
        if os.path.exists("./katas/" + file_name):
            affirmative_response = ["y", "yes", "yeah", "yup", ".", "bruh"]
            response = ""

            while response is False:
                response = input("Kata: " + title + " already exists. Do you want to overwrite it?").lower()

            # continue if they want to overwrite the file
            if response in affirmative_response:
                file = open("./katas/" + file_name, "w")
                file.write(kata_template(solution))

            # if you don't want to overwrite you will continue onto the next file
            else:
                continue

        else:
            # this will create the file if it didn't exist before
            file = open("./katas/" + file_name, "w")
            file.write(kata_template(solution))


def main():
    # login to code wars
    codeWars = login()

    # grab all the solutions
    solutions = get_solutions(codeWars)

    # write the solutions
    write_solutions(solutions)


if __name__ == "__main__":
    main()
