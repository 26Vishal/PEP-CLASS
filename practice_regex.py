#Write a syntax to validate a mobile no

import re
mobile = input("Enter mobile number:")
if re.match(r'^[6-9]\d{9}$',mobile):
    print("Vaild no")
else:
    print("Invalid mobile number")