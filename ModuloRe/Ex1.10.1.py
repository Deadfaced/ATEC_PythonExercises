import re

text = "2024"
pattern = r"^\d{4}$"

result = re.fullmatch(pattern, text)

if result:
    print("Valid room code")
else:
    print("Invalid room code")