#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if exists
                               # would exists on all but last line
        # IF the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
# no need to close our file - closed automatically
