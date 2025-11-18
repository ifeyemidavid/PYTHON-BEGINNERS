

s1 = 'hello'
s2 = ' world!'
s3 = "this is " \
"a multi-line " \
"string."

print(s1 + s2)
print(s3)

s = "programming"
print(s[0])
print(s[-1])
print(s[3:7])
print(s[::-1])

# using common strings method
text = "Python3 Programming"
stripped = text.strip()
upper = text.upper()
replaced = stripped.replace("Python3", "Python")
split_words = replaced.split()
joined = "-".join(split_words)

print(f"stripped: '{stripped}'")
print(f"upper: {upper}")
print(f"replaced: {replaced}")
print(f"split words: {split_words}")
print(f"joined: {joined}")

# string formatting practice

name = "alice"
score = 95.6789

print("student: %s, score: %.2f" %(name, score))
print(f"student: {name}, score: {score:.2f}")

import re

# regular expression example
text = "contact us at support@example.com or sales@example.org"
emails = re.findall(r'\w+@\w+\.\w+',text)

print(emails)