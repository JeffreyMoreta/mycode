#!/usr/bin/env python3
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# challenge attempt
_, _, [goggles, eyes], nothing = challenge
print(f"My {eyes}! The {goggles} do {nothing}!")

# trial attempt
_, _, face, nothing  = trial
print(f"My {face['goggles']}! The {face['eyes']} do {nothing}!")

# nightmare attempt
goggles = nightmare[0]["kumquat"]
eyes = nightmare[0]["user"]["name"]["first"]
nothing = nightmare[0]["d"]
print(f"My {eyes}! The {goggles} do {nothing}!")
