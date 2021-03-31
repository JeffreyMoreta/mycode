#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0 # counter for success
badips = []

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            badips.append(line.split("from ")[1][0:-1])
        if "- - - - -] Loaded" in line:
            loginsuccess += 1

print("The number of failed log in attempts is", loginfail, badips)
print("The number of succesful log in attempts is", loginsuccess)
