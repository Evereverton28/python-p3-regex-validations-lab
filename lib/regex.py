import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[A-Z][a-zA-Z]*(?:[ '-][A-Za-z]+)*$"
name_regex = re.compile(name)

phone_number = r"^\+?[1-9]\d{0,2}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$|^\d{3}-\d{3}-\d{4}$|^\(\d{3}\)\s?\d{3}-\d{4}$|^\d{10}$"
phone_regex = re.compile(phone_number)

email_address = r"^[a-zA-Z_.+-][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email_regex = re.compile(email_address)
