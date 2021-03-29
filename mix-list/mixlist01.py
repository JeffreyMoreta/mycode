#!/usr/bin/env python3

# create a list containing three items
my_list = ["192.168.0.5", 5060, "UP"]

# display the first itme in the list
print("The first item in the list (IP): " + my_list[0])
# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]))
# display the third item in the list
print("The last item in the list (state): " + my_list[2])

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print(f"When I {new_list[-1]} into IP addresses {new_list[3]} or {new_list[-2]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}.")
