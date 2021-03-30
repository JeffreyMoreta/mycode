#!/usr/bin/env python3
questions = {
        "character": "Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)",
        "stat": "Which statistic do you want to know about? (real name, powers, archenemy)"
        }

char_name = input(questions["character"]).lower()
char_stat = input(questions["stat"]).lower()

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
        }
print(f"{char_name.title()}'s {char_stat} is: {heroes[char_name][char_stat]}")
