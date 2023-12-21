import re

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# pattern = r"[A-Z]+yclone"
# text = "Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March"
# match = re.search(pattern, text)
# print(match)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Define a regular expression pattern
# pattern = r"expression"
# Match the pattern against a string
# text = "Hello, world!"
# match = re.search(pattern, text)

# if match:
#     print("Match found!")
# else:
#     print("Match not found.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# pattern = r"[a-z]+at"
# text = "The cat is in the hat."

# matches = re.findall(pattern, text)

# print(matches)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

text = "The email is shardendumishra01@gmail.com"
pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)

if match:
    email = match.group()
    print(email)
