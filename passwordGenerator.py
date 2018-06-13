# PasswordGenerator.py - This script will generate a password that meets all
# of the following criteria -
#   At least one upper and lowercase character
#   At least one number
#   At least one special character/symbol
#   Is at least 10 characters long

import re, pyperclip as pc, random as r

# Random length password between 10-16 characters
pwlength = r.randint(10,16)

# All valid characters that can be used in the password
characters = (
    "abcdefghijklmnopqrstuvwxyz" +          # lowercase
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +          # upeprcase
    "0123456789" +                          # numbers
    "!\"£$%^&*()-_+=[{]};:'@#~,<.>/?\\|")   # special characters

# Turn characters into a list and shuffle them a couple of times
charlist = list(characters)
r.shuffle(charlist)
r.shuffle(charlist)

# Regular expression to check that password meets all criteria
upperregex = re.compile(r'[A-Z]')
lowerregex = re.compile(r'[a-z]')
digitregex = re.compile(r'\d')
specialregex = re.compile(r'[\!\"\£\$\%\^\&\*\(\)\-\_\+\=\[\{\]\}\;\:\'\@\#\~\,\<\.\>\/\?\\\|]')

password = ''

# Loop through each character for the password, picking a random one until
# the length is complete and all criteria are met
while True:
    for i in range(pwlength):
        randnum = r.randint(0,len(charlist))
        password += charlist[randnum]

    if upperregex.search(password) == None:
        continue
    elif lowerregex.search(password) == None:
        continue
    elif digitregex.search(password) == None:
        continue
    elif specialregex.search(password) == None:
        continue
    else:
        break

pc.copy(password)
print(password)



