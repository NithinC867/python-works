# word="hello"

# print(word.capitalize())
# print(word.upper())
# print(word.casefold())
# print(word.lower())
# print(word.index("e"))

word="i have 2 bike and 1 car"

for ch in word:
    if ch.isalpha():
        print(ch,end=",")

print("")
for ch in word:
    if ch.isdigit():
        print(ch,end=",")