import re

text = "My phone number is 9876543210. My age is 18."

# Search for a number
result = re.search(r"\d+", text)
print("First number:", result.group())

# Find all numbers
numbers = re.findall(r"\d+", text)
print("All numbers:", numbers)

# Match a phone number
phone = re.search(r"\b\d{10}\b", text)

if phone:
    print("Phone number found:", phone.group())
else:
    print("Phone number not found")
